#include <iostream>
using namespace std;

#define MAX_N 6

typedef struct _Point {
	int r;
	int c;
	int sum;

	_Point() {
		r = 0;
		c = 0;
		sum = 0;
	}

	_Point(int _r, int _c, int _sum) {
		r = _r;
		c = _c;
		sum = _sum;
	}
} Point;

Point stack[MAX_N];
int top;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int map[5][5], visited[1000000], ans = 0, mul[5] = {10, 100, 1000, 10000, 100000};

void stackInit();
int stackIsEmpty();
int stackIsFull();
int stackPush(Point p);
int stackPop(Point* p);
void dfs(int depth, int r, int c, int sumNum);

int main() {
	for (int r = 0; r < 5; ++r) {
		for (int c = 0; c < 5; ++c) {
			scanf("%d", &map[r][c]);
		}
	}
	
	for (int r = 0; r < 5; ++r) {
		for (int c = 0; c < 5; ++c) {
			dfs(0, r, c, map[r][c]);
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

void dfs(int depth, int r, int c, int sumNum) {
	if (depth == 6) {
		if (visited[sumNum]) return;
		++ans;
		visited[sumNum]++;
		return;
	}

	for (int d = 0; d < 4; ++d) {
		int nr = r + dr[d];
		int nc = c + dc[d];
		if (nr < 0 || nr >= 5 || nc < 0 || nc >= 5) continue;
		dfs(depth + 1, nr, nc, sumNum + map[nr][nc] * mul[depth]);
	}
}