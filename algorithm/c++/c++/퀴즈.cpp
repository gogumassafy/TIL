#include <stdio.h>

int T, N;


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		int result;
		result = N * (N + 1) * (2 * N + 1) / 6;
		result %= 1000000007
		printf("#%d %d\n", tc, result);
	}

	return 0;
}