#include <iostream>
using namespace std;

#define MAX_N 8

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

int front, rear;
Point queue[MAX_N];

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

char map[5][6];
int ans = 0, visited[5][5], selected[5][5];

void visitedClear();
void dfs(int depth, int yCnt, int k);
bool bfs();
void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point p);
int queueDeque(Point* p);

int main() {
	for (int r = 0; r < 5; ++r) {
		scanf("%s", map[r]);
	}

	for (int i = 0; i < 25; ++i) {
		int yCnt = 0;
		if (map[i / 5][i % 5] == 'Y') ++yCnt;
		selected[i / 5][i % 5] = 1;
		queue[0] = Point(i / 5, i % 5);
		dfs(1, yCnt, i);
		selected[i / 5][i % 5] = 0;
	}

	printf("%d", ans);
	return 0;
}

void visitedClear() {
	for (int r = 0; r < 5; ++r) {
		for (int c = 0; c < 5; ++c) {
			visited[r][c] = 0;
		}
	}
}

void queueInit() {
	front = 0;
	rear = 1;
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
	return 1;
}

int queueDeque(Point* p) {
	if (queueIsEmpty()) return 0;
	
	*p = queue[front++];
	return 1;
}

void dfs(int depth, int yCnt, int k) {
	// Y >= 4보다 같다면 return;
	if (yCnt >= 4) {
		return;
	}

	if (depth == 7) {
		// 실제 인접해있는지 체크
		queueInit();
		visitedClear();
		visited[queue[0].r][queue[0].c] = 1;
		if (bfs()) ++ans;
		return;
	}

	for (int i = k + 1; i < 25; ++i) {
		int isY = 0;
		if (map[i / 5][i % 5] == 'Y') ++isY;
		selected[i / 5][i % 5] = 1;
		dfs(depth + 1, yCnt + isY, i);
		selected[i / 5][i % 5] = 0;
	}
}

bool bfs() {
	Point now;
	int count = 1;
	while (!queueIsEmpty()) {
		queueDeque(&now);
		for (int d = 0; d < 4; ++d) {
			int nr = now.r + dr[d];
			int nc = now.c + dc[d];

			if (nr < 0 || nr >= 5 || nc < 0 || nc >= 5) continue;
			if (visited[nr][nc]) continue;
			if (!selected[nr][nc]) continue;
			
			visited[nr][nc] = 1;
			queuePush(Point(nr, nc));
			++count;
		}
	}
	if (count < 7) return false;
	return true;
}