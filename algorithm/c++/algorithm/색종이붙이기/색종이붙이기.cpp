#include <iostream>
using namespace std;

#define MAX_NUM 987654321

int ans = MAX_NUM, total = 0;
int raw[10][10], countPaper[6];
void dfs(int depth, int sum);
void del(int r, int c, int n);
void reset(int r, int c, int n);
bool check(int r, int c, int n);

int main() {
	for (int i = 0; i < 6; ++i) countPaper[i] = 5;


	for (int r = 0; r < 10; ++r) {
		for (int c = 0; c < 10; ++c) {
			scanf("%d", &raw[r][c]);
			if (raw[r][c] == 1) ++total;
		}
	}

	dfs(0, 0);

	if (ans == MAX_NUM) ans = -1;
	printf("%d", ans);

	return 0;
}

void dfs(int sr, int sum) {
	if (sum >= ans) return;
	if (total == 0) {
		if (ans > sum) ans = sum;
		return;
	}

	for (int r = sr; r < 10; ++r) {
		for (int c = 0; c < 10; ++c) {
			if (raw[r][c] == 0) continue;

			for (int d = 5; d > 0; --d) {
				if (countPaper[d] == 0) continue;
				if (!check(r, c, d)) continue;
				del(r, c, d);
				dfs(r, sum + 1);
				reset(r, c, d);
			}

			return;
		}
	}
}

void del(int r, int c, int n) {
	for (int i = r; i < r + n; ++i) {
		for (int j = c; j < c + n; ++j) {
			raw[i][j] = 0;
		}
	}
	countPaper[n]--;
	total -= n * n;
}

void reset(int r, int c, int n) {
	for (int i = r; i < r + n; ++i) {
		for (int j = c; j < c + n; ++j) {
			raw[i][j] = 1;
		}
	}
	countPaper[n]++;
	total += n * n;
}

bool check(int r, int c, int n) {
	for (int i = r; i < r + n; ++i) {
		for (int j = c; j < c + n; ++j) {
			if (i >= 10 || j >= 10) return false;
			if (raw[i][j] == 0) return false;
		}
	}
	return true;
}