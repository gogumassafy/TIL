#include <iostream>
using namespace std;

int N, map[100][100];
long long countNum[100][100];

long long dfs(int r, int c);

int main() {
	scanf("%d", &N);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf("%d", &map[r][c]);
		}
	}

	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			countNum[r][c] = -1;
		}
	}

	printf("%lld", dfs(0, 0));
	return 0;
}

long long dfs(int r, int c) {
	if (r == N - 1 && c == N - 1) {
		return 1;
	}

	if (r >= N || c >= N || map[r][c] == 0) return 0;

	if (countNum[r][c] > 0) return countNum[r][c];

	countNum[r][c] = dfs(r + map[r][c], c) + dfs(r, c + map[r][c]);
	return countNum[r][c];

}