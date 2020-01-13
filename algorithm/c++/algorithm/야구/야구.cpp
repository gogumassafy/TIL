#include <iostream>
using namespace std;

int N, input[50][10], order[9] = { 0, }, visited[10] = { 0, }, outCount, ans;

void dfs(int depth);
void calculate();

int main() {
	scanf("%d", &N);
	ans = 0;
	for (int i = 0; i < N; ++i) {
		for (int j = 1; j <= 9; ++j) {
			scanf("%d", &input[i][j]);
		}
	}
	dfs(0);
	printf("%d", ans);
	return 0;
}

void dfs(int depth) {
	if (depth == 9) {
		outCount = 0;
		calculate();
		return;
	}
	if (depth == 3) {
		order[depth] = 1;
		dfs(depth + 1);
		return;
	}

	// depth는 0부터 8까지 선수들의 idx 순서를 저장
	// i는 선수들의 idx를 의미 1부터 9까지.
	for (int i = 2; i <= 9; ++i) {
		if (visited[i]) continue;
		order[depth] = i;
		visited[i] = 1;
		dfs(depth + 1);
		visited[i] = 0;
	}
}

void calculate() {
	int ening = 0, idx = 0, current, temp = 0, mound[5] = { 0, };
	while (ening < N) {
		outCount = 0;
		for (int i = 0; i < 4; ++i) {
			mound[i] = 0;
		}
		while (outCount < 3) {
			current = order[(idx++) % 9];
			if (input[ening][current] == 0) {
				++outCount;
				continue;
			}
			else {
				mound[0] = 1;
				for (int i = 3; i >= 0; --i) {
					if (i + input[ening][current] >= 4) {
						mound[4] += mound[i];
						mound[i] = 0;
					}
					else {
						mound[i + input[ening][current]] = mound[i];
						mound[i] = 0;
					}
				}
			}
		}
		++ening;
	}
	temp += mound[4];
	if (temp > ans) ans = temp;
}