#include <iostream>
using namespace std;

#define MAX_N 10001
#define INF 987654321

typedef struct _Point {
	int r;
	int c;

	_Point() {
		r = 0;
		c = 0;
	}

	_Point(int _r, int _c) {
		r = _r;
		c = _c;
	}
} Point;

Point queue[MAX_N];
int front, rear;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int N, map[100][100], visited[100][100], ans = INF;

void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point p);
int queueDeque(Point* p);
void coloring(int color);
void bfs(int color);
void visitedClear();

int main() {
	scanf("%d", &N);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf("%d", &map[r][c]);
		}
	}
	int color = 1;
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			if (visited[r][c]) continue;
			if (map[r][c] == 0) continue;
			queueInit();
			queuePush(Point(r, c));
			visited[r][c] = color;
			coloring(color++);
		}
	}


	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			if (map[r][c] == 0) continue;
			queueInit();
			visitedClear();
			queuePush(Point(r, c));
			bfs(visited[r][c]);
		}
	}

	printf("%d", ans);
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

void coloring(int color) {
	Point now;
	while (!queueIsEmpty()) {
		queueDeque(&now);
		for (int d = 0; d < 4; ++d) {
			int nr = now.r + dr[d];
			int nc = now.c + dc[d];
			if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
			if (map[nr][nc] == 0) continue;
			if (visited[nr][nc]) continue;

			visited[nr][nc] = color;
			queuePush(Point(nr, nc));
		}
	}
}

void bfs(int color) {
	Point now;
	int distance = -1, time = 0;
	while (!queueIsEmpty()) {
		time = (rear - front + MAX_N) % MAX_N;
		while (time--) {
			queueDeque(&now);
			if (visited[now.r][now.c] != 9 && visited[now.r][now.c] != color) {
				// 답을 갱신해준다.
				if (distance < ans) ans = distance;
				return;
			}

			if (ans <= distance) return;
			for (int d = 0; d < 4; ++d) {
				int nr = now.r + dr[d];
				int nc = now.c + dc[d];
				if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
				if (visited[nr][nc] == 9 || visited[nr][nc] == color) continue;
				if (visited[nr][nc] == 0) {
					visited[nr][nc] = 9;
				}

				queuePush(Point(nr, nc));
			}
		}
		++distance;
	}
}

void visitedClear() {
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			if (visited[r][c] == 9) visited[r][c] = 0;
		}
	}
}