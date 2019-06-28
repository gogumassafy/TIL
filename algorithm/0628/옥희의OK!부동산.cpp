#include <stdio.h>
int T, N, M, arr[10000], result, temp, first;


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		result = 0, temp = 0, first = 0;
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &arr[i]);
		}
		for (int i = 0; i < N; ++i) {
			temp += arr[i];
			while (temp > M) {
				temp -= arr[first];
				++first;
			}
			if (temp == M) {
				++result;
				temp -= arr[first];
				++first;
			}
		}
		printf("#%d %d\n", tc, result);
	}
	return 0;
}