#include <iostream>
using namespace std;

#define MAX_N 40001

typedef struct _Point {
	int r;
	int c;
	int d;
	int distance;
	_Point() {
		r = 0;
		c = 0;
		d = 0;
		distance = 0;
	}

	// µ¿ ¼­ ³² ºÏ
	// 1  2  3  4
	// ³² µ¿ ºÏ ¼­
	// 0  1  2  3

	_Point(int _d) {
		r = 0;
		c = 0;
		distance = 0;
		if (_d == 2) {
			d = 3;
		}
		else if (_d == 3) {
			d = 0;
		}
		else if (_d == 4) {
			d = 2;
		}
		else {
			d = _d;
		}
	}

	_Point(int _r, int _c, int _d, int _distance) {
		r = _r;
		c = _c;
		d = _d;
		distance = _distance;
	}
} Point;

Point queue[MAX_N];
int front, rear;

// ³² µ¿ ºÏ ¼­
int dr[4] = { 1, 0, -1, 0 };
int dc[4] = { 0, 1, 0, -1 };

int N, M, map[100][100], visited[4][100][100], ans;

void bfs(Point* goal);
void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point value);
int queueDeque(Point* value);

int main() {
	scanf("%d %d", &N, &M);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%d", &map[r][c]);
		}
	}

	int r, c, dir;
	scanf("%d %d %d", &r, &c, &dir);
	Point start(dir);
	start.r = r - 1, start.c = c - 1;
	scanf("%d %d %d", &r, &c, &dir);
	Point goal(dir);
	goal.r = r - 1, goal.c = c - 1;

	queuePush(start);
	visited[start.d][start.r][start.c] = 1;

	bfs(&goal);

	printf("%d", ans);
	return 0;
}

void bfs(Point* goal) {
	Point now;
	
	while (!queueIsEmpty()) {
		queueDeque(&now);
		if (now.r == goal->r && now.c == goal->c && now.d == goal->d) {
			ans = now.distance;
			return;
		}
		

		int nr = now.r, nc = now.c;
		for (int i = 1; i < 4; ++i) {
			nr += dr[now.d];
			nc += dc[now.d];
			if (nr < 0 || nr >= N || nc < 0 || nc >= M) break;
			if (map[nr][nc]) break;
			if (visited[now.d][nr][nc]) continue;
			visited[now.d][nr][nc] = 1;
			queuePush(Point(nr, nc, now.d, now.distance + 1));
		}

		int nd;
		for (int i = 0; i < 2; ++i) {
			if (i) {
				nd = (now.d + 1) % 4;
				if (visited[nd][now.r][now.c]) continue;
			}
			else {
				nd = (now.d + 3) % 4;
				if (visited[nd][now.r][now.c]) continue;
			}
			visited[nd][now.r][now.c] = 1;
			queuePush(Point(now.r, now.c, nd, now.distance + 1));
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

int queuePush(Point value) {
	if (queueIsFull()) {
		return 0;
	}

	queue[rear++] = value;
	if (rear == MAX_N) rear = 0;
	return 1;
}

int queueDeque(Point* value) {
	if (queueIsEmpty()) {
		return 0;
	}

	*value = queue[front++];
	if (front == MAX_N) front = 0;
	return 1;
}