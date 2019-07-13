#include <iostream>
#include <string.h>
using namespace std;

int T, N, M, s, e, c, result, arr[401][401], visit[401] = { 0, }, start;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &M);
		memset(arr, 20000, sizeof(arr));

		result = 987654321;
		for (int m = 0; m < M; ++m) {
			scanf("%d %d %d", &s, &e, &c);
			arr[s][e] = c;
		}
		for (int i = 1; i < N + 1; ++i) {
			for (int j = 1; j < N + 1; ++j) {
				for (int k = 1; k < N + 1; ++k) {
					if (arr[j][k] > arr[j][i] + arr[i][k]) {
						arr[j][k] = arr[j][i] + arr[i][k];
					}
				}
			}
		}
		for (int i = 1; i < N + 1; ++i) {
			if (result > arr[i][i]) {
				result = arr[i][i];
			}
		}
		if (result == 987654321)
			result = -1;
		printf("#%d %d\n", tc, result);
	}
	return 0;
}