#include <iostream>
using namespace std;


// µ¿ ¼­ ºÏ ³²
int dr[4] = { 0, 0, -1, 1 };
int dc[4] = { 1, -1, 0, 0 };
int dice[6] = { 0, };

int N, M, X, Y, K, map[20][20], instruct[1000];

void dfs();

int main() {
	scanf("%d %d %d %d %d", &N, &M, &X, &Y, &K);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%d", &map[r][c]);
		}
	}
	for (int k = 0; k < K; ++k) {
		scanf("%d", &instruct[k]);
		--instruct[k];
	}
	dfs();
	return 0;
}

void dfs() {
	int r = X, c = Y, d, top = 0;
	for (int k = 0; k < K; ++k) {
		d = instruct[k];
		int nr = r + dr[d];
		int nc = c + dc[d];
		
		if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
		// ³²
		if (d == 3) {
			int pre = dice[3], pro;
			for (int i = 0; i < 4; ++i) {
				pro = dice[i];
				dice[i] = pre;
				pre = pro;
			}
		}
		// ºÏ
		else if (d == 2) {
			int pre = dice[0], pro;
			for (int i = 3; i >= 0; --i) {
				pro = dice[i];
				dice[i] = pre;
				pre = pro;
			}
		}
		// ¼­
		else if (d == 1) {
			int pre, pro;
			pre = dice[0];
			dice[0] = dice[5];
			pro = dice[4];
			dice[4] = pre;
			pre = dice[2];
			dice[2] = pro;
			dice[5] = pre;
		}
		// µ¿
		else {
			int pre, pro;
			pre = dice[0];
			dice[0] = dice[4];
			pro = dice[5];
			dice[5] = pre;
			pre = dice[2];
			dice[2] = pro;
			dice[4] = pre;
		}
		if (map[nr][nc]) {
			dice[2] = map[nr][nc];
			map[nr][nc] = 0;
		}
		else {
			map[nr][nc] = dice[2];
		}
		r = nr, c = nc;
		printf("%d\n", dice[0]);
	}
}