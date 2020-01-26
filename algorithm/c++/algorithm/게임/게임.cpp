#include <iostream>
using namespace std;

#define MAX_N 2501

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

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

int front;
int rear;
Point queue[MAX_N];

int N, M, ans = 0;
int board[50][50];
int visited[50][50];
char tmp;

void bfs();
void queueInit();
int queueIsEmpty();
int queueIsFull();
int queueEnqueue(Point value);
int queueDequeue(Point* value);

int main() {
	scanf("%d %d", &N, &M);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf(" %c", &tmp);
			board[r][c] = tmp - '0';
		}
	}
	queueEnqueue(Point());
	visited[0][0] = 0;
	bfs();
	printf("%d", ans);
	return 0;
}

void bfs() {
	Point p(0, 0);
	int count = 0, time;
	while (!queueIsEmpty()) {
		time = rear > front ? rear - front : front - rear;
		for (int i = 0; i < time; ++i) {
			queueDequeue(&p);
			if (board[p.r][p.c] > 9) continue;
			for (int d = 0; d < 4; ++d) {
				int nr = dr[d] * board[p.r][p.c] + p.r;
				int nc = dc[d] * board[p.r][p.c] + p.c;
				if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
					ans = count > ans ? count : ans;
					continue;
				}
				if (visited[nr][nc]) {
					//ans = -1;
					continue;
				}
				queueEnqueue(Point(nr, nc));
				visited[nr][nc] = 1;
			}
		}
		++count;
	}
	ans = count > ans ? count : ans;
}

void queueInit() {
	front = 0;
	rear = 0;
}

int queueIsEmpty() {
	return (front == rear);
}

int queueIsFull() {
	if ((rear + 1) % MAX_N == front) return 1;
	else return 0;
}

int queueEnqueue(Point value) {
	if (queueIsFull()) {
		return 0;
	}
	queue[rear] = value;
	++rear;
	if (rear == MAX_N) rear = 0;
	return 1;
}

int queueDequeue(Point* value) {
	if (queueIsEmpty()) {
		return 0;
	}
	*value = queue[front];
	++front;
	if (front == MAX_N) front = 0;
	return 1;
}