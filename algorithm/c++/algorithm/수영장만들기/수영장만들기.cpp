#include <iostream>
using namespace std;

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

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int N, M, ans = 0, temp = 0;
int swimingPool[50][50], visited[50][50];
Point stack[2500];

int top = 0;
void stackInit();
int stackPush(Point P);
int stackPop(Point* p);
bool stackIsEmpty();
bool stackIsFull();
void visitedClear();
int dfs(int i);

int main() {
	scanf("%d %d", &N, &M);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%1d", &swimingPool[r][c]);
		}
	}
	
	for (int i = 2; i < 10; ++i) {
		stackInit();
		visitedClear();
		for (int r = 1; r < N - 1; ++r) {
			for (int c = 1; c < M - 1; ++c) {
				if (visited[r][c]) continue;
				if (swimingPool[r][c] >= i) continue;
				visited[r][c] = 1;
				stackPush(Point(r, c));
				ans += dfs(i);
			}
		}
	}

	printf("%d\n", ans);
	return 0;
}

void stackInit() {
	top = 0;
}

bool stackIsEmpty() {
	return top == 0;
}

bool stackIsFull() {
	return top == 2500;
}

int stackPush(Point p) {
	if (stackIsFull()) {
		printf("full");
		return 0;
	}
	stack[top++] = p;
	return 1;
}

int stackPop(Point* p) {
	if (stackIsEmpty()) {
		printf("empty");
		return 0;
	}
	*p = stack[--top];
	return 1;
}

void visitedClear() {
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			visited[r][c] = 0;
		}
	}
}

int dfs(int i) {
	Point P;
	int temp = i - swimingPool[stack[0].r][stack[0].c], flag = 0;
	++swimingPool[stack[0].r][stack[0].c];
	while (!stackIsEmpty()) {
		stackPop(&P);
		
		for (int d = 0; d < 4; ++d) {
			int nr = P.r + dr[d];
			int nc = P.c + dc[d];

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (visited[nr][nc]) continue;
			if (swimingPool[nr][nc] >= i) continue;
			if (nr == 0 || nr == (N - 1) || nc == 0 || nc == (M - 1)) {
				flag = 1;
			}
			++temp;
			++swimingPool[nr][nc];
			visited[nr][nc] = 1;
			stackPush(Point(nr, nc));
		}
	}
	if (flag) return 0;
	return temp;
}