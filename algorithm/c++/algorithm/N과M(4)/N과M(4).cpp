#include <iostream>
using namespace std;

int result[9];

void dfs(int start, int depth, int N, int M);

int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	dfs(1, 0, N, M);
	return 0;
}

void dfs(int start, int depth, int N, int M) {
	if (depth == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", result[i]);
		}
		printf("\n");
		return;
	}

	for (int i = start; i <= N; ++i) {
		result[depth] = i;
		dfs(i, depth + 1, N, M);
	}
	return;
}