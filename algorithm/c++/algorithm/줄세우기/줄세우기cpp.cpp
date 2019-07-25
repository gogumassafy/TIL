#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int T, N, countNum[60000], arr[5000], flag, tempInput, tail;


void dfs(int depth);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		flag = 0;
		tail = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &tempInput);
			if (countNum[tempInput]++ == 0) {
				arr[tail++] = tempInput;
			}
		}
		sort(arr, arr + tail);
		printf("#%d ", tc);
		dfs(0);
		printf("\n");
	}
	return 0;
}

void dfs(int depth) {
	if (depth == N) {
		return;
	}
	if (countNum[arr[depth]] == 0) {
		dfs(depth + 1);
		return;
	}
	if (arr[depth] + 1 == arr[depth + 1] && countNum[arr[depth + 1]]) {
		if (depth + 2 >= tail) {
			for (int i = 0; i < countNum[arr[depth + 1]]; ++i) {
				printf("%d ", arr[depth + 1]);
			}
			countNum[arr[depth + 1]] = 0;
		}
		for (int i = 0; i < countNum[arr[depth]]; ++i) {
			printf("%d ", arr[depth]);
		}
		countNum[arr[depth]] = 0;
		if (depth + 2 < tail) {
			printf("%d ", arr[depth + 2]);
			countNum[arr[depth + 2]]--;
		}
	}
	else {
		for (int i = 0; i < countNum[arr[depth]]; ++i) {
			printf("%d ", arr[depth]);
		}
		countNum[arr[depth]] = 0;
	}
	dfs(depth + 1);
}