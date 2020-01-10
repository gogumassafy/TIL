#include <iostream>
using namespace std;

#define MAX_N 100000

int front;
int rear;
int N, M, K;
int input[1000][1000], visited[1000][1000][11];
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

typedef struct {
	int length;
	int r;
	int c;
	int bomb;
} Point;

Point queue[MAX_N];

void queueInit(void)
{
	front = 0;
	rear = 0;
}

int queueIsEmpty(void)
{
	return (front == rear);
}

int queueIsFull(void)
{
	if ((rear + 1) % MAX_N == front)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int queueEnqueue(Point value)
{
	if (queueIsFull())
	{
		printf("queue is full!");
		return 0;
	}
	queue[rear] = value;
	rear++;
	if (rear == MAX_N)
	{
		rear = 0;
	}

	return 1;
}

int queueDequeue(Point *value)
{
	if (queueIsEmpty())
	{
		// printf("queue is empty!");
		return 0;
	}
	*value = queue[front];
	front++;
	if (front == MAX_N)
	{
		front = 0;
	}
	return 1;
}


int bfs();

int main() {
	scanf("%d %d %d", &N, &M, &K);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%1d", &input[r][c]);
		}
	}
	Point start = { 1, 0, 0 , K };
	queueInit();
	queueEnqueue(start);
	visited[0][0][K] = 1;
	printf("%d", bfs());
	return 0;
}

int bfs() {
	Point p, next;
	while (!queueIsEmpty()) {
		queueDequeue(&p);
		if (p.r == (N - 1) && p.c == (M - 1)) return p.length;
		for (int d = 0; d < 4; ++d) {
			int nr = p.r + dr[d];
			int nc = p.c + dc[d];
			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (visited[nr][nc][p.bomb]) continue;
			if (input[nr][nc]) {
				if (p.bomb < 1) continue;
				else {
					next = { p.length + 1, nr, nc, p.bomb - 1 };
					queueEnqueue(next);
				}
			}
			else {
				next = { p.length + 1, nr, nc, p.bomb };
				queueEnqueue(next);
			}
			visited[nr][nc][next.bomb] = 1;
		}
	}
	return -1;
}