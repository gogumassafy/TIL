#include <iostream>
using namespace std;

int T, N, K, arr[100000][30];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &K);
		for (int r = 0; r < N; ++r) {
			for (int c = 0; c < K; ++c) {
				scanf("%d", arr[r][c]);
			}
		}
		printf("#%d %d", tc);
	}
	return 0;
}