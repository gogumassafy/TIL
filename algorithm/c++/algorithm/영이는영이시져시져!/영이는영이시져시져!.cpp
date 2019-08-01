#include <iostream>
#include <cmath>
using namespace std;

int T, N, dr[2] = { 1, 0 }, dc[2] = { 0, 1 }, arr[1000][1000], result, countZero;

void dfs(int sr, int sc, long long total);

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		result = 987654321;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &arr[i][j]);
			}
		}
		dfs(0, 0, arr[0][0]);
		printf("#%d %d\n", tc, result);
	}
	return 0;
}

void dfs(int sr, int sc, long long total) {
	if (result != 987654321) {
		int limit = pow(10, result);
		if (total % limit == 0) {
			return;
		}
	} 
	if (sr == N - 1 && sc == N - 1) {
		countZero = 0;
		while (!(total % 10)) {
			countZero++;
			total /= 10;
		}
		if (result > countZero) {
			result = countZero;
		}
		return;
	}
	int nr, nc;
	for (int i = 0; i < 2; ++i) {
		nr = sr + dr[i];
		nc = sc + dc[i];
		if (nr >= N || nc >= N) {
			continue;
		}
		if (arr[nr][nc] == 0) {
			continue;
		}
		dfs(nr, nc, total * (long long) arr[nr][nc]);
	}
	return;
}