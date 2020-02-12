#include <iostream>
using namespace std;

#define MAX_N 2501

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


// ¼­ ºÏ µ¿ ³²
int dr[4] = { 0, -1, 0, 1 };
int dc[4] = { -1, 0, 1, 0 };

int N, M, map[50][50], visited[50][50], totalRoom = 0, maxRoomCnt = 0, sumCnt = 0, checked[MAX_N], roomCnt[MAX_N];

void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point p);
int queueDeque(Point* p);
void bfs();

int main() {
	scanf("%d %d", &N, &M);
	for (int r = 0; r < M; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf("%d", &map[r][c]);
		}
	}

	for (int r = 0; r < M; ++r) {
		for (int c = 0; c < N; ++c) {
			if (visited[r][c]) continue;
			++totalRoom;
			visited[r][c] = totalRoom;
			queuePush(Point(r, c));
			bfs();
		}
	}

	printf("%d\n", totalRoom);
	printf("%d\n", maxRoomCnt);
	printf("%d\n", sumCnt);
	return 0;
}

void queueInit() {
	front = 0;
	rear = 0;
	return;
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
	int temp = 0;
	int maxLinked = 0;

	for (int i = 1; i < MAX_N; ++i) {
		if (i == totalRoom) checked[i] = 0;
		else checked[i] = 1;
	}

	while (!queueIsEmpty()) {
		queueDeque(&now);
		++temp;
		for (int d = 0; d < 4; ++d) {
			int nr = now.r + dr[d];
			int nc = now.c + dc[d];

			if (nr < 0 || nr >= M || nc < 0 || nc >= N) continue;
			if (visited[nr][nc]) {
				if (checked[visited[nr][nc]]) {
					if (roomCnt[visited[nr][nc]] > maxLinked) maxLinked = roomCnt[visited[nr][nc]];
					checked[visited[nr][nc]] = 0;
				}
				continue;
			}
			if ((1 << d) & map[now.r][now.c]) continue;

			visited[nr][nc] = totalRoom;
			queuePush(Point(nr, nc));
		}
	}
	if (temp > maxRoomCnt) maxRoomCnt = temp;
	roomCnt[totalRoom] = temp;
	if (temp + maxLinked > sumCnt) sumCnt = temp + maxLinked;
}