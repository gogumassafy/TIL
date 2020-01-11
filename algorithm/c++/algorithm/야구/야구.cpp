#include <iostream>
using namespace std;

int N, input[50][10], order[9] = { 4, }, visited[10] = { 0, }, outCount;

void dfs(int depth);

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		for (int j = 1; j <= 9; ++j) {
			scanf("%d", &input[i][j]);
		}
	}
	dfs(1);
	return 0;
}

void dfs(int depth) {
	if (depth == 9) {
		outCount = 0;
		calculate();
		return;
	}

	// depth는 0부터 8까지 선수들의 idx 순서를 저장
	// i는 선수들의 idx를 의미 1부터 9까지.
	for (int i = 1; i <= 9; ++i) {
		if (i == 4 || visited[i]) continue;
		order[depth] = i;
		visited[i] = 1;
		dfs(depth + 1);
		visited[i] = 0;
	}
}

void calculate() {
	int ening = 0, idx = 0, current;
	while (ening < N) {
		outCount = 0;
		while (outCount < 3) {
			current = order[idx++];
			if (input[ening][current] == 0) {
				++outCount;
				continue;
			}
			else {

			}
		}
		++ening;
	}
}