#include <iostream>
using namespace std;

#define MAX_NUM 987654321

int N, M, ans = MAX_NUM;
char raw[51][51];
const char sol[2][9] = {"WBWBWBWB", "BWBWBWBW"};

int check(int r, int c, int color);

int main() {
	int temp;
	scanf("%d%d", &N, &M);

	for (int r = 0; r < N; ++r) {
		scanf(" %[^\n]", &raw[r]);
	}

	for (int r = 0; r < N - 7; ++r) {
		for (int c = 0; c < M - 7; ++c) {
			for (int col = 0; col < 2; ++col) {
				temp = check(r, c, col);
				ans = temp < ans ? temp : ans;
			}
		}
	}
	printf("%d\n", ans);
	return 0;
}

int check(int r, int c, int color) {
	int cnt = 0;
	for (int i = 0; i < 8; ++i) {
		for (int j = 0; j < 8; ++j) {
			if (cnt >= ans) return MAX_NUM;
			if (sol[color][j] != raw[r + i][c + j]) ++cnt;
		}
		color = (color + 1) % 2;
	}

	return cnt;
}