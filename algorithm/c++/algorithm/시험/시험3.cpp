#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/time.h>

#define WORKER_SLEEP_US 50000
#define ASSERT_SLEEP_US 100000
#define ASSERT_TMOUT_MS 5000

typedef struct _rwlock_t rwlock_t;

// thread cycle
// NONE -> WAIT -> (lock) -> LOCK -> (unlock) -> DONE
typedef enum {
	STATE_NONE,     // thread가 아직 생성되지 않은 상태
	STATE_WAIT,     // thread가 read or write을 하려고 대기 중인 상태
	STATE_LOCK,     // thread가 read or write을 하는 중인 상태 (lock acquired)
	STATE_DONE,     // thread가 read or write를 끝내고 종료된 상태
} work_state;

typedef struct _worker_t {
	bool running;
	void *fn;
	work_state state;
	pthread_t thread;
	pthread_mutex_t lock;
	rwlock_t *rwlock;
} worker_t;

typedef struct _workers_t {
	worker_t *readers;
	worker_t *writers;
	size_t nreaders;
	size_t nwriters;
} workers_t;


typedef struct _rwlock_t {
    // pthread_mutex_t와 pthread_cond_t를 사용하여 구현하세요.
    // pthread_rwlock_t는 사용하실 수 없습니다.

	pthread_mutex_t w_mutex;

} rwlock_t;

rwlock_t *rwlock_new(void)
{
    // rwlock을 새로 할당하고 초기화하여 리턴합니다.
    rwlock_t *rwlock;
    
    rwlock = malloc(sizeof(rwlock_t));
    
    // 여기서 rwlock의 각종 멤버 변수들을 초기화하세요.
	rwlock.w_mutex = PTHREAD_MUTEX_INITIALIZER
    
    return rwlock;
}

void rwlock_destroy(rwlock_t *rwlock)
{
    // rwlock이 사용한 메모리를 정리합니다.
    if (rwlock == NULL)
        return;
    
    // 여기서 rwlock의 각종 멤버 변수들을 제거하세요.
    
    free(rwlock);
}

void read_lock(rwlock_t *rwlock)
{
    // reader가 rwlock을 lock 합니다.

	while (rwlock)
}

void read_unlock(rwlock_t *rwlock)
{
    // reader가 rwlock을 unlock 합니다.
}

void write_lock(rwlock_t *rwlock)
{
    // writer가 rwlock을 lock 합니다.
}

void write_unlock(rwlock_t *rwlock)
{
    // writer가 rwlock을 unlock 합니다.
}


static void *worker_read(void *arg)
{
	worker_t *w = arg;

	pthread_mutex_lock(&w->lock);
	w->state = STATE_WAIT;
	pthread_mutex_unlock(&w->lock);

	read_lock(w->rwlock);

	pthread_mutex_lock(&w->lock);
	w->state = STATE_LOCK;
	pthread_mutex_unlock(&w->lock);

	while (w->running) {
		usleep(WORKER_SLEEP_US);
	}

	read_unlock(w->rwlock);

	pthread_mutex_lock(&w->lock);
	w->state = STATE_DONE;
	pthread_mutex_unlock(&w->lock);

	return NULL;
}

static void *worker_write(void *arg)
{
	worker_t *w = arg;

	pthread_mutex_lock(&w->lock);
	w->state = STATE_WAIT;
	pthread_mutex_unlock(&w->lock);

	write_lock(w->rwlock);

	pthread_mutex_lock(&w->lock);
	w->state = STATE_LOCK;
	pthread_mutex_unlock(&w->lock);

	while (w->running) {
		usleep(WORKER_SLEEP_US);
	}

	write_unlock(w->rwlock);

	pthread_mutex_lock(&w->lock);
	w->state = STATE_DONE;
	pthread_mutex_unlock(&w->lock);

	return NULL;
}

static void worker_init(workers_t *workers, int n, int m, rwlock_t *rwlock)
{
	int i;
	worker_t *w;

	workers->readers = n > 0 ? calloc(n, sizeof(worker_t)) : NULL;
	workers->writers = m > 0 ? calloc(m, sizeof(worker_t)) : NULL;
	workers->nreaders = n;
	workers->nwriters = m;

	for (i = 0; i < n; i++) {
		w = &workers->readers[i];
		w->fn = worker_read;
		w->running = false;
		w->state = STATE_NONE;
		w->rwlock = rwlock;
		pthread_mutex_init(&w->lock, NULL);
	}

	for (i = 0; i < m; i++) {
		w = &workers->writers[i];
		w->fn = worker_write;
		w->running = false;
		w->state = STATE_NONE;
		w->rwlock = rwlock;
		pthread_mutex_init(&w->lock, NULL);
	}
}

static void worker_start(worker_t *w)
{
	w->running = true;
	pthread_create(&w->thread, NULL, w->fn, w);
}

static void worker_finish(worker_t *w)
{
	w->running = false;
}

static void worker_finish_writer(workers_t *workers)
{
	worker_t *w;
	int i;
	for (i = 0; i < workers->nwriters; i++) {
		w = &workers->writers[i];
		pthread_mutex_lock(&w->lock);
		if (STATE_LOCK == w->state) {
			w->running = false;
			pthread_mutex_unlock(&w->lock);
			break;
		}
		pthread_mutex_unlock(&w->lock);
	}
}

static bool worker_assert(workers_t *workers, work_state state, int n, int m)
{
	int readers, writers, i;
	struct timeval tv1, tv2;
	unsigned long elapsed_ms = 0;
	worker_t *w;

	gettimeofday(&tv1, NULL);
	while (elapsed_ms < ASSERT_TMOUT_MS) {
		readers = 0;
		writers = 0;

		for (i = 0; i < workers->nreaders; i++) {
			w = &workers->readers[i];
			pthread_mutex_lock(&w->lock);
			if (state == w->state)
				readers++;
			pthread_mutex_unlock(&w->lock);
		}
		for (i = 0; i < workers->nwriters; i++) {
			w = &workers->writers[i];
			pthread_mutex_lock(&w->lock);
			if (state == w->state)
				writers++;
			pthread_mutex_unlock(&w->lock);
		}

		if (readers == n && writers == m)
			return true;

		usleep(ASSERT_SLEEP_US);
		gettimeofday(&tv2, NULL);
		elapsed_ms = (tv2.tv_sec - tv1.tv_sec) * 1000 + (tv2.tv_usec - tv1.tv_usec) / 1000;
	}

	return false;
}

static void workers_cleanup(workers_t *workers)
{
	worker_t *w;
	int i;
	for (i = 0; i < workers->nreaders; i++) {
		w = &workers->readers[i];
		pthread_join(w->thread, NULL);
		pthread_mutex_destroy(&w->lock);
	}
	for (i = 0; i < workers->nwriters; i++) {
		w = &workers->writers[i];
		pthread_join(w->thread, NULL);
		pthread_mutex_destroy(&w->lock);
	}
	free(workers);
}

static int parse_n_m(char *s, int *n, int *m)
{
	char *last;
	char *p = strchr(s, ' ');
	if (!p)
		return -1;

	*p = '\0';
	*n = (int) strtol(s, &last, 10);
	if ('\0' != *last)
		return -1;

	*m = (int) strtol(p + 1, &last, 10);
	if ('\n' != *last && ' ' != *last && '\0' != *last)
		return -1;

	return 0;
}

static worker_t *parse_worker(char *s, workers_t *workers)
{
	if ('r' != *s && 'w' != *s)
		return NULL;

	char *last;
	int id = (int) strtol(s + 1, &last, 10) - 1;
	if ('\n' != *last)
		return NULL;

	return 'r' == *s ? &workers->readers[id] : &workers->writers[id];
}

int main(void)
{
	int ret;
	char line[512];
	FILE *infp = stdin;
	FILE *outfp = fopen(getenv("OUTPUT_PATH"), "w");

	int *n = malloc(sizeof(int));
	int *m = malloc(sizeof(int));
	workers_t *workers = calloc(1, sizeof(workers_t));
	worker_t *w;
	work_state state;

	rwlock_t *rwlock = rwlock_new();

	while (!feof(infp)) {
		if (!fgets(line, sizeof(line), infp))
			break;

		// trim comment
		char *c = strchr(line, '#');
		if (c)
			*c = '\0';

		if (strncmp(line, "init ", 5) == 0) {
			ret = parse_n_m(line + 5, n, m);
			if (ret < 0) {
				fprintf(outfp, "err on parsing init\n");
				return 1;
			}
			worker_init(workers, *n, *m, rwlock);

		} else if (strncmp(line, "start ", 6) == 0) {
			w = parse_worker(line + 6, workers);
			if (!w) {
				fprintf(outfp, "err on parsing start\n");
				break;
			}
			worker_start(w);

		} else if (strncmp(line, "finish ", 7) == 0) {
			if (strncmp(line + 7, "writer", 6) == 0) {
				worker_finish_writer(workers);
			} else {
				w = parse_worker(line + 7, workers);
				if (!w) {
					fprintf(outfp, "err on parsing finish\n");
					break;
				}
				worker_finish(w);
			}

		} else if (strncmp(line, "assert ", 7) == 0) {
			state = STATE_NONE;

			if (strncmp(line + 7, "wait ", 5) == 0) {
				state = STATE_WAIT;
			} else if (strncmp(line + 7, "lock ", 5) == 0) {
				state = STATE_LOCK;
			} else if (strncmp(line + 7, "done ", 5) == 0) {
				state = STATE_DONE;
			}
			if (STATE_NONE != state) {
				ret = parse_n_m(line + 12, n, m);
				if (ret < 0) {
					fprintf(outfp, "err on parsing assert\n");
					return 1;
				}

				if (worker_assert(workers, state, *n, *m)) {
					fprintf(outfp, "ok\n");
				} else {
					fprintf(outfp, "fail\n");
				}
			}
		}
	}

	workers_cleanup(workers);
	rwlock_destroy(rwlock);
	free(n);
	free(m);
    fclose(infp);
    fclose(outfp);

	return 0;
}

int rwlock_wrlock(rwlock_t* rwlock, DWORD milliseconds)
{
	DWORD code = WaitForSingleObject(rwlock->write_mutex, milliseconds);
	switch (code)
	{
	case WAIT_TIMEOUT: return 0;
	default:
		if (rwlock->readers) {
			code = milliseconds
				? WaitForSingleObject(rwlock->read_event, milliseconds)
				: WAIT_TIMEOUT;
			if ((code == WAIT_FAILED) || (code == WAIT_TIMEOUT)) {
				/* Unable to wait for readers to finish, release write lock: */
				if (!ReleaseMutex(rwlock->write_mutex))
	case WAIT_FAILED: return -1;
				else {
					;
				} return ((code == WAIT_TIMEOUT) ? 0 : -1);
			}
		}
	} return 1;
}