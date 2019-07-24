#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int T, N, countNum[5000], arr[5000], result[5000], flag, tempInput, tail;


void dfs(int depth, int num);


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
		dfs(0, 0);
		printf("#%d ", tc);
		for (int i = 0; i < N; ++i) {
			printf("%d ", result[i]);
		}
		printf("\n");
	}
	return 0;
}

void dfs(int depth, int num) {
	if (flag) {
		return;
	}
	if (depth == N) {
		flag = 1;
		return;
	}
	int temp;
	for (int i = num; i < tail; ++i) {
		temp = arr[i];
		if (countNum[temp] == 0) {
			continue;
		}
		if (temp + 1 == arr[i + 1] && i + 2 >= tail && countNum[temp + 1]) {
			continue;
		}
		if (depth > 0) {
			if (temp == result[depth - 1] + 1)
				temp = arr[i + 1];
		}
		countNum[temp]--;
		result[depth] = temp;
		dfs(depth + 1, num);
		if (flag) {
			return;
		}
		countNum[temp]++;
	}
}