#include <iostream>
using namespace std;

typedef struct _Point {
	int r;
	int c;
	_Point() {
		r = -1;
		c = -1;
	}
	_Point(int nr, int nc) {
		r = nr;
		c = nc;
	}
} Point;

int N, M, D, temp, ans = 0, r, c;
int raw[16][15], map[16][15], visited[15] = { 0, };
Point archer[3];

void reset();
void selectPosition(int depth, int k);
void enemiesDown();
int shot();

int main() {
	scanf("%d%d%d", &N, &M, &D);

	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%d", &raw[r][c]);
		}
	}

	selectPosition(0, 0);

	printf("%d\n", ans);
	return 0;
}

void selectPosition(int depth, int k) {
	if (depth == 3) {
		temp = 0;
		reset();
		for (int i = 0; i < N; ++i) {
			temp += shot();
			enemiesDown();
		}
		if (temp > ans) ans = temp;
		return;
	}
	
	for (int i = k; i < M - 2 + depth; ++i) {
		if (visited[i]) continue;
		visited[i] = 1;
		map[N][i] = 9;
		archer[depth].r = N;
		archer[depth].c = i;
		selectPosition(depth + 1, i + 1);
		visited[i] = 0;
		map[N][i] = 0;
	}
}

void reset() {
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			map[r][c] = raw[r][c];
		}
	}
}

void enemiesDown() {
	for (int r = N - 1; r >= 0; --r) {
		for (int c = 0; c < M; ++c) {
			if (map[r][c] == 0) continue;
			if (r != N - 1) map[r + 1][c] = 1;
			map[r][c] = 0;
		}
	}

	return;
}

int shot() {
	int nr, flag = 0, temp = 0;
	Point target[3];

	for (int i = 0; i < 3; ++i) {
		flag = 0;
		r = archer[i].r;
		c = archer[i].c;
		for (int d = 1; d <= D; ++d) {
			nr = r;
			for (int nc = c - d; nc <= c + d; ++nc) {
				if (nc >= 0 && nc < M) {
					if (map[nr][nc] == 1) {
						flag = 1;
						target[i] = Point(nr, nc);
						break;
					}
				}
				if (nc < c) --nr;
				else ++nr;
			}
			if (flag) break;
		}
	}
	
	for (int i = 0; i < 3; ++i) {
		r = target[i].r;
		c = target[i].c;
		if (r == -1) continue;
		temp += map[r][c];
		map[r][c] = 0;
	}
	return temp;
}