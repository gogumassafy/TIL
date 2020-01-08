// https://www.acmicpc.net/problem/15663
#include <iostream>
using namespace std;

int N, M, arr[8], ans[8], visited[8] = { 0, };

void quickSort(int first, int last) {
	int pivot;
	int i;
	int j;
	int temp;

	if (first < last) {
		pivot = first;
		i = first;
		j = last;

		while (i < j) {
			while (arr[i] <= arr[pivot] && i < last) {
				++i;
			}
			while (arr[j] > arr[pivot]) {
				--j;
			}
			if (i < j) {
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
		temp = arr[pivot];
		arr[pivot] = arr[j];
		arr[j] = temp;

		quickSort(first, j - 1);
		quickSort(j + 1, last);
	}
}

void dfs(int depth, int start) {
	if (depth == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", ans[i]);
		}
		printf("\n");
		return;
	}

	for (int i = 0; i < N; ++i) {
		if (visited[i]) continue;
		if (i > 0 && visited[i - 1] == 0 && arr[i - 1] == arr[i]) continue;
		ans[depth] = arr[i];
		visited[i] = 1;
		dfs(depth + 1, i + 1);
		visited[i] = 0;
	}

}

int main() {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &arr[i]);
	}
	quickSort(0, N - 1);
	dfs(0, 0);
	return 0;
}