#include <iostream>
using namespace std;
 
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int N, M, map[500][500], visited[500][500];

int dp(int r, int c);

int main() {
	scanf("%d %d", &N, &M);


	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%d", &map[r][c]);
			visited[r][c] = -1;
		}
	}

	printf("%d", dp(0, 0));
	return 0;
}

int dp(int r, int c) {
	if (r == N - 1 && c == M - 1) return 1;
	if (visited[r][c] == -1) visited[r][c] = 0;
	for (int d = 0; d < 4; ++d) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
		if (map[nr][nc] >= map[r][c]) continue;
		if (visited[nr][nc] >= 0) {
			visited[r][c] += visited[nr][nc];
			continue;
		}
		visited[r][c] += dp(nr, nc);
	}

	return visited[r][c];
}