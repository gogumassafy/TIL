#include <iostream>
using namespace std;

#define MAX_N 5001

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

	_Point(int _r, int _c, int _d, int _distance) {
		r = _r;
		c = _c;
		d = _d;
		distance = _distance;
	}

} Point;

int front, rear;
Point queue[MAX_N];


int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int N, visited[2][50][50], ans;
char map[50][50];
Point goal;

void bfs();
void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point p);
int queueDeque(Point* p);

int main() {
	scanf("%d", &N);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf(" %c", &map[r][c]);
		}
	}
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			if (map[r][c] == 'B') {
				if (r - 1 >= 0 && map[r - 1][c] == 'B' && visited[1][r - 1][c] == 0) {
					queuePush(Point(r, c, 1, 0));
					visited[1][r][c] = 1;
				}
				else if (c - 1 >= 0 && map[r][c - 1] == 'B' && visited[0][r][c - 1] == 0) {
					queuePush(Point(r, c, 0, 0));
					visited[0][r][c] = 1;
				}
			}
			else if (map[r][c] == 'E') {
				if (r - 1 >= 0 && map[r - 1][c] == 'E' && goal.r == 0 && goal.c == 0) {
					goal.r = r, goal.c = c, goal.d = 1;
				}
				else if (c - 1 >= 0 && map[r][c - 1] == 'E' && goal.r == 0 && goal.c == 0) {
					goal.r = r, goal.c = c, goal.d = 0;
				}
			}
		}
	}

	bfs();

	printf("%d", ans);
	return 0;
}

void bfs() {
	Point now;
	while (!queueIsEmpty()) {
		queueDeque(&now);

		if (now.r == goal.r && now.c == goal.c && now.d == goal.d) {
			ans = now.distance;
			return;
		}

		for (int d = 0; d < 5; ++d) {
			int nd, nhr, nhc, nmr, nmc, nlr, nlc;
			if (d < 4) {
				nd = now.d;
				nmr = now.r + dr[d];
				nmc = now.c + dc[d];
			}
			else {
				// 회전 할 때 주변 3*3 공간 비어있는지 체크 안했다..
				nd = (now.d + 1) % 2;
				nmr = now.r;
				nmc = now.c;
				if (nmr < 1 || nmr >= N - 1 || nmc < 1 || nmc >= N - 1) continue;
				if (map[nmr - 1][nmc - 1] == '1' || map[nmr - 1][nmc + 1] == '1' || map[nmr +  1][nmc + 1] == '1' || map[nmr + 1][nmc - 1] == '1') continue;

			}

			if (nd) {
				nhr = nmr - 1;
				nhc = nmc;
				nlr = nmr + 1;
				nlc = nmc;
			}
			else {
				nhr = nmr;
				nhc = nmc - 1;
				nlr = nmr;
				nlc = nmc + 1;
			}

			if (nmr < 0 || nmr >= N || nmc < 0 || nmc >= N) continue;
			if (nhr < 0 || nhr >= N || nhc < 0 || nhc >= N) continue;
			if (nlr < 0 || nlr >= N || nlc < 0 || nlc >= N) continue;
			if (map[nhr][nhc] == '1' || map[nmr][nmc] == '1' || map[nlr][nlc] == '1') continue;
			if (visited[nd][nmr][nmc]) continue;
			
			visited[nd][nmr][nmc] = 1;
			queuePush(Point(nmr, nmc, nd, now.distance + 1));
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