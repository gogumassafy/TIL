#include <iostream>
using namespace std;

#define INF 987654321

int N, selected[20], powerMap[20][20], ans = INF, half;

void dfs(int depth, int k);
void calculatePower();

int main() {
	scanf("%d", &N);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf("%d", &powerMap[r][c]);
		}
	}
	half = N / 2;
	dfs(0, 0);

	printf("%d", ans);
	return 0;
}

void dfs(int depth, int k) {
	if (depth == half) {
		calculatePower();
		return;
	}

	for (int i = k; i < N; ++i) {
		selected[i] = 1;
		dfs(depth + 1, i + 1);
		selected[i] = 0;
	}
}

void calculatePower() {
	// left´Â 1, right´Â 0
	int score[2] = { 0, 0 }, temp = INF;
	
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (selected[i] != selected[j]) continue;
			score[selected[i]] += powerMap[i][j];
		}
	}
	if (score[0] > score[1]) {
		temp = score[0] - score[1];
	}
	else temp = score[1] - score[0];

	if (temp < ans) ans = temp;
}