#include <iostream>
using namespace std;

// ╩С го аб ©Л
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int N, ans = 0, input[6][20][20];


void dfs(int depth);
void clear(int depth);

int main() {
	scanf("%d", &N);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf("%d", &input[0][r][c]);
		}
	}

	printf("%d", ans);
	return 0;
}

void dfs(int depth) {
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			if (input[depth][r][c] > ans) {
				ans = input[depth][r][c];
			}
		}
	}

	if (depth == 5) return;

	for (int i = 0; i < 4; ++i) {
		clear(depth + 1);

	}
}

void clear(int depth) {
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			input[depth][r][c] = 0;
		}
	}
}