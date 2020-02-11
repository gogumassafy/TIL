#include <iostream>
using namespace std;

#define MAX_N 900

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

Point stack[MAX_N];
int top = 0;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int T, M, N, K, X, Y, map[50][50], ans;

void mapClear();
void dfs();
void stackInit();
int stackIsEmpty();
int stackIsFull();
int stackPush(Point p);
int stackPop(Point* p);

int main() {
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc) {
		ans = 0;
		scanf("%d %d %d", &M, &N, &K);
		stackInit();
		for (int k = 0; k < K; ++k) {
			scanf("%d %d", &X, &Y);
			map[Y][X] = 1;
		}

		for (int r = 0; r < N; ++r) {
			for (int c = 0; c < M; ++c) {
				if (map[r][c]) {
					stackPush(Point(r, c));
					map[r][c] = 0;
					++ans;
					dfs();
				}
			}
		}
		printf("%d\n", ans);
	}

	return 0;
}

void mapClear() {
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			map[r][c] = 0;
		}
	}
}

void stackInit() {
	top = 0;
	ans = 0;
}

int stackIsEmpty() {
	return top == 0;
}

int stackIsFull() {
	return top == MAX_N;
}

int stackPush(Point p) {
	if (stackIsFull()) return 0;

	stack[top++] = p;
	return 1;
}

int stackPop(Point* p) {
	if (stackIsEmpty()) return 0;

	*p = stack[--top];
	return 1;
}

void dfs() {
	Point now;
	while (!stackIsEmpty()) {
		stackPop(&now);

		for (int d = 0; d < 4; ++d) {
			int nr = now.r + dr[d];
			int nc = now.c + dc[d];

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (map[nr][nc] == 0) continue;

			map[nr][nc] = 0;
			stackPush(Point(nr, nc));
		}
	}
}