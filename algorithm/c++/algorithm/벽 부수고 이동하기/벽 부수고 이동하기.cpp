#include <iostream>
using namespace std;

#define MAX_N 2000000

typedef struct _Point {
	int r;
	int c;
	int k;

	_Point() {
		r = 0;
		c = 0;
		k = 1;
	}

	_Point(int _r, int _c, int _k) {
		r = _r;
		c = _c;
		k = _k;
	}
} Point;

Point queue[MAX_N];
int front, rear;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int N, M, map[1000][1000], visited[2][1000][1000];

void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point p);
int queueDeque(Point* p);
void bfs();

int main() {
	scanf("%d %d", &N, &M);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%1d", &map[r][c]);
		}
	}
	bfs();
	return 0;
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
	if (queueIsFull()) return 0;

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

void bfs() {
	Point now;
	queuePush(Point());
	visited[1][0][0] = 1;
	while (!queueIsEmpty()) {
		queueDeque(&now);
		if (now.r == N - 1 && now.c == M - 1) {
			printf("%d", visited[now.k][now.r][now.c]);
			return;
		}
		for (int d = 0; d < 4; ++d) {
			int bombCnt = now.k;
			int nr = now.r + dr[d];
			int nc = now.c + dc[d];

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (map[nr][nc]) {
				if (now.k < 1) continue;
				--bombCnt;
			}
			if (visited[bombCnt][nr][nc]) continue;
			visited[bombCnt][nr][nc] = visited[now.k][now.r][now.c] + 1;
			queuePush(Point(nr, nc, bombCnt));
		}
	}
	printf("-1");
}