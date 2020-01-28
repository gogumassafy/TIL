#include <iostream>
using namespace std;

#define MAX_N 40001

typedef struct _Point {
	int r;
	int c;
	int k;
	int distance;

	_Point() {
		r = 0;
		c = 0;
		k = 0;
		distance = 0;
	}

	_Point(int _r, int _c, int _k, int _distance) {
		r = _r;
		c = _c;
		k = _k;
		distance = _distance;
	}

} Point;

Point queue[MAX_N];
int front, rear;


int dr[12] = { -1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2 };
int dc[12] = { 0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1 };

int K, N, M, map[200][200], visited[30][200][200], ans = -1;

void bfs();
void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point p);
int queueDeque(Point* p);

int main() {
	scanf("%d %d %d", &K, &M, &N);
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; ++c) {
			scanf("%d", &map[r][c]);
		}
	}
	queueInit();
	visited[K][0][0] = 1;
	queuePush(Point(0, 0, K, 0));
	bfs();

	printf("%d", ans);
	return 0;
}

void bfs() {
	Point p;
	while (!queueIsEmpty()) {
		queueDeque(&p);
		if (p.r == N - 1 && p.c == M - 1) {
			ans = p.distance;
			return;
		}
		for (int d = 0; d < 12; ++d) {
			int nk = p.k;
			if (d >= 4) {
				if (nk == 0) continue;
				--nk;
			}
			int nr = dr[d] + p.r;
			int nc = dc[d] + p.c;

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (map[nr][nc]) continue;
			if (visited[nk][nr][nc]) continue;

			visited[nk][nr][nc] = 1;
			queuePush(Point(nr, nc, nk, p.distance + 1));
		}
	}
}

void queueInit() {
	front = 0;
	rear = 0;
}
int queueIsEmpty() {
	return front == rear;
}

int queueIsFull() {
	return (rear + 1) % MAX_N == front;
}

int queuePush(Point p) {
	if (queueIsFull()) {
		return 0;
	}
	queue[rear++] = p;
	if (rear == MAX_N) rear = 0;

	return 1;
}

int queueDeque(Point* p) {
	if (queueIsEmpty()) return 0;

	*p = queue[front++];
	if (front == MAX_N) front = 0;

	return 1;
}