#include <iostream>
using namespace std;

int input[8], result[8], visited[8];

void dfs(int depth, int N, int M);
void QS(int first, int end);

int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &input[i]);
	}
	QS(0, N - 1);
	dfs(0, N, M);
	return 0;
}

void dfs(int depth, int N, int M) {
	if (depth == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", result[i]);
		}
		printf("\n");
		return;
	}

	for (int i = 0; i < N; ++i) {
		if (visited[i]) continue;
		result[depth] = input[i];
		visited[i] = 1;
		dfs(depth + 1, N, M);
		visited[i] = 0;
	}
	return;
}

void QS(int first, int end) {
	int pivot;
	int i;
	int j;
	int temp;

	if (first < end) {
		pivot = first;
		i = first;
		j = end;

		while (i < j) {
			while (input[i] <= input[pivot] && i < end) {
				++i;
			}
			while (input[j] > input[pivot]) {
				--j;
			}
			if (i < j) {
				temp = input[i];
				input[i] = input[j];
				input[j] = temp;
			}
		}
		
		temp = input[pivot];
		input[pivot] = input[j];
		input[j] = temp;

		QS(first, j - 1);
		QS(j + 1, end);
	}
}