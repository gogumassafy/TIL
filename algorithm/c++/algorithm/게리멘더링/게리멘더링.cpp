#include <iostream>
using namespace std;

int N, arr[11], route[11][11], K, e, selected[11] = { 0, }, ans = 987654321;

void check() {
	
}

void combination(int depth, int s, int end) {
	if (depth == end) {
		check();
		return;
	}
	for (int i = s; i <= N; ++i) {
		if (ans == 0) {
			return;
		}
		selected[i] = 1;
		combination(depth + 1, i + 1, end);
		selected[i] = 0;
	}
	return;
}

int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; ++i) {
		scanf("%d", &arr[i]);
	}
	for (int i = 1; i <= N; ++i) {
		scanf("%d", &K);
		for (int k = 0; k < K; ++k) {
			scanf("%d", &e);
			route[i][e] = 1;
		}
	}
	for (int i = 1; i <= N / 2; ++i) {
		if (ans == 0) {
			break;
		}
		combination(0, 1, i);
	}
	printf("%d", ans);
	return 0;
}