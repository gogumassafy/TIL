#include <iostream>
using namespace std;


int T, R, C, result, dr[4] = { -1, 1, 0, 0 }, dc[4] = { 0, 0, -1, 1 }, visit[20][20] = { 0, }, alphabet[26] = { 0, }, temp;
char arr[20][20];


void dfs(int depth, int sr, int sc);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		result = 0;
		scanf("%d %d", &R, &C);
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				scanf(" %c", &arr[r][c]);
			}
		}
		temp = arr[0][0] - 'A';
		visit[0][0] = 1;
		alphabet[temp] = 1;
		dfs(1, 0, 0);
		visit[0][0] = 0;
		alphabet[temp] = 0;
		printf("#%d %d\n", tc, result);
	}
	return 0;
}

void dfs(int depth, int sr, int sc) {
	int nr, nc, temp;

	if (depth > result) {
		result = depth;
	}

	for (int i = 0; i < 4; ++i) {
		nr = sr + dr[i];
		nc = sc + dc[i];
		if (nr >= R || nr < 0 || nc >= C || nc < 0) {
			continue;
		}
		if (visit[nr][nc]) {
			continue;
		}
		temp = arr[nr][nc] - 'A';
		if (alphabet[temp]) {
			continue;
		}
		visit[nr][nc] = 1;
		alphabet[temp] = 1;
		dfs(depth + 1, nr, nc);
		visit[nr][nc] = 0;
		alphabet[temp] = 0;
	}
	return;
}
