#include <iostream>
using namespace std;

#define MAX_Num 1000

typedef struct {
	int diskIdx;
	int numIdx;
} Point;

int N, M, T, ans, key, top;
int disk[51][50], command[50][3], temp[50], dir[2] = { 1, -1 };
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
float averageNum;
Point stack[MAX_Num];

void rotate(int x, int d, int k);
void stackInit(void);
int dfs(int x);
int stackIsEmpty();
int stackIsFull();
int stackPush(Point value);
int stackPop(Point* value);
float avg();

int main() {
	scanf("%d %d %d", &N, &M, &T);
	for (int i = 1; i <= N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf("%d", &disk[i][j]);
		}
	}
	for (int i = 0; i < T; ++i) {
		scanf("%d %d %d", &command[i][0], &command[i][1], &command[i][2]);
	}

	for (int i = 0; i < T; ++i) {
		rotate(command[i][0], command[i][1], command[i][2]);
	}

	//for (int r = 1; r <= N; ++r) {
	//	for (int c = 0; c < M; ++c) {
	//		ans += disk[r][c];
	//	}
	//}
	avg();
	printf("%d", ans);
	return 0;
}

void rotate(int x, int d, int k) {
	// d가 0일 경우 시계 방향, 1은 반시계 방향.
	// k는 거리
	int n = dir[d] * k;

	for (int current = x; current <= N; current += x) {
		for (int i = 0; i < M; ++i) {
			temp[i] = disk[current][i];
		}


		for (int i = 0; i < M; ++i) {
			// 시계
			disk[current][(i + n + M) % M] = temp[i];
		}
	}
	if (!dfs(x)) {
		// 평균 구하는 연산
		averageNum = avg();
		for (int r = 1; r <= N; ++r) {
			for (int c = 0; c < M; ++c) {
				if (disk[r][c] == 0) continue;
				if (disk[r][c] > averageNum) disk[r][c] -= 1;
				else if (disk[r][c] < averageNum) disk[r][c] += 1;
			}
		}
	}
	return;
}

int dfs(int x) {
	int flag = 0;
	for (int r = 1; r <= N; ++r) {
		for (int c = 0; c < M; ++c) {
			if (disk[r][c] == 0) continue;
			top = 0;
			key = disk[r][c];
			disk[r][c] = 0;
			Point p = { r, c };
			Point Next = { r, c };
			stackPush(p);
			while (!stackIsEmpty()) {
				stackPop(&p);
				for (int d = 0; d < 4; ++d) {
					int nr = p.diskIdx + dr[d];
					int nc = (p.numIdx + dc[d] + M) % M;
					if (nr <= 0 || nr > N ) continue;
					if (disk[nr][nc] == 0) continue;
					if (disk[nr][nc] != key) continue;
					flag = 1;
					disk[nr][nc] = 0;
					Next = { nr, nc };
					stackPush(Next);
				}
			}
			if (p.diskIdx == r && p.numIdx == c) disk[r][c] = key;
		}
	}
	return flag;
}

void stackInit(void) {
	top = 0;
}

int stackIsEmpty() {
	return (top == 0);
}

int stackIsFull() {
	return (top == MAX_Num);
}

int stackPush(Point value) {
	if (stackIsFull()) {
		return 0;
	}
	stack[top] = value;
	top++;
	return 1;
}

int stackPop(Point* value) {
	if (top == 0) {
		return 0;
	}
	top--;
	*value = stack[top];
	return 1;
}

float avg() {
	float count = 0;
	ans = 0;
	for (int r = 1; r <= N; ++r) {
		for (int c = 0; c < M; ++c) {
			if (disk[r][c]) {
				count += 1;
				ans += disk[r][c];
			}
		}
	}
	return ans / count;
}