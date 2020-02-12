#include <iostream>
using namespace std;

#define MAX_N 9;

int length[9], visited[9], flag = 1;

void quickSort(int first, int last);
void dfs(int depth, int k, int sum);

int main() {
	for (int i = 0; i < 9; ++i) {
		scanf("%d", &length[i]);
	}

	quickSort(0, 8);
	dfs(0, 0, 0);

	return 0;
}

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
			while (length[i] <= length[pivot]) {
				++i;
			}
			while (length[j] > length[pivot]) {
				--j;
			}
			if (i < j) {
				temp = length[i];
				length[i] = length[j];
				length[j] = temp;
			}
		}

		temp = length[pivot];
		length[pivot] = length[j];
		length[j] = temp;

		quickSort(first, j - 1);
		quickSort(j + 1, last);
	}
}

void dfs(int depth, int k, int sum) {
	if (sum > 100 || flag == 0) return;
	if (depth == 7 && sum == 100) {
		for (int i = 0; i < 9; ++i) {
			if (visited[i]) printf("%d\n", length[i]);
		}
		exit(0);
		return;
	}

	int temp = 0;

	for (int i = k; i < 9; ++i) {
		if (visited[i]) continue;
		temp = sum + length[i];
		if (temp > 100) return;
		visited[i] = 1;
		dfs(depth + 1, i + 1, sum + length[i]);
		visited[i] = 0;
	}
}