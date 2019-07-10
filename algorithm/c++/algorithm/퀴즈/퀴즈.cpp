#include <stdio.h>

int T, N;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		int temp = N * (1 + N) / 2;
		printf("#%d %d\n", tc, temp);
	}
	return 0;
}