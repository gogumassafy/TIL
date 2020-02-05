#include <iostream>
using namespace std;

#define MAX_N 1000000

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
int top;


int qdr[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int qdc[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };

int kdr[8] = { -2, -2, -1, -1, 1, 1, 2, 2 };
int kdc[8] = { -1, 1, -2, 2, -2, 2, -1, 1 };

int N, M, Q, K, P, map[1000][1000], ans;

void stackInit();
int stackIsEmpty();
int stackIsFull();
int stackPush(Point p);
int stackPop(Point* p);
void dfs(int mal);

int main() {
	scanf("%d %d", &N, &M);
	scanf("%d", &Q);
	int r, c;

	for (int q = 0; q < Q; ++q) {
		scanf("%d %d", &r, &c);
		map[r - 1][c - 1] = 9;
	}

	scanf("%d", &K);
	for (int k = 0; k < K; ++k) {
		scanf("%d %d", &r, &c);
		map[r - 1][c - 1] = 8;
	}

	scanf("%d", &P);
	for (int p = 0; p < P; ++p) {
		scanf("%d %d", &r, &c);
		map[r - 1][c - 1] = 7;
	}


	ans = N * M - (Q + K + P);
	
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			if (map[r][c] < 8) continue;
			stackInit();
			stackPush(Point(r, c));
			dfs(map[r][c]);
		}
	}
	
	printf("%d", ans);
	return 0;
}

void stackInit() {
	top = 0;
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

void dfs(int mal) {
	Point now;
	while (!stackIsEmpty()) {
		stackPop(&now);
		if (mal == 9) {
			for (int d = 0; d < 8; ++d) {
				int nr = now.r;
				int nc = now.c;
				while (1) {
					nr += qdr[d];
					nc += qdc[d];
					if (nr < 0 || nr >= N || nc < 0 || nc >= M) break;
					if (map[nr][nc] >= 6) break;

					if (map[nr][nc] == 0) --ans;
					map[nr][nc] = 1;
				}
			}
		}
		else {
			for (int d = 0; d < 8; ++d) {
				int nr = now.r + kdr[d];
				int nc = now.c + kdc[d];
				if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
				if (map[nr][nc]) continue;
				--ans;
				map[nr][nc] = 1;
			}
		}
	}
}