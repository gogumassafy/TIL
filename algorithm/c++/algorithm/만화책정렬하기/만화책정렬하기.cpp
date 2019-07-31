#include <iostream>
using namespace std;

int T, N, result, arr[200001], countBook, head, temp;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		result = 1;
		countBook = 0;
		head = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &temp);
			arr[temp] = i;
		}
		for (int i = 1; i < N; ++i) {
			if (arr[i] > arr[i + 1]) {
				result++;
			}
		}
		printf("#%d %d\n", tc, result);
	}
	return 0;
}