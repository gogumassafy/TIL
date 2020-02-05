#include <iostream>
using namespace std;

// ºÏ µ¿ ³² ¼­
int dr[4] = { -1, 0, 1, 0 };
int dc[4] = { 0, 1, 0, -1 };

int N, M, R, C, D, map[50][50], ans = 1;

void dfs();

int main() {
	scanf("%d %d", &N, &M);
	scanf("%d %d %d", &R, &C, &D);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%d", &map[r][c]);
		}
	}

	dfs();
	printf("%d\n", ans);
	return 0;
}

void dfs() {
	int r = R, c = C, d = D, sd = D;
	map[r][c] = 9;
	while (1) {
		int nr, nc, flag = 0;
		for (int i = 0; i < 4; ++i) {
			d = (d + 3) % 4;
			nr = r + dr[d];
			nc = c + dc[d];

			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (map[nr][nc]) continue;

			flag = 1;
			map[nr][nc] = 9;
			r = nr, c = nc;
			++ans;
			break;
		}

		if (flag) continue;
		nr = r - dr[d];
		nc = c - dc[d];

		if (nr < 0 || nr >= N || nc < 0 || nc >= M) break;
		if (map[nr][nc] == 1) break;

		r = nr, c = nc;
	}
}