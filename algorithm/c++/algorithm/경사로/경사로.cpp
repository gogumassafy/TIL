#include <iostream>
using namespace std;

int N, L, map[100][100], ans = 0;

int main() {
	scanf("%d %d", &N, &L);

	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf("%d", &map[r][c]);
		}
	}

	// 가로 검사
	for (int r = 0; r < N; ++r) {
		int flag = 1, cnt = 1;
		for (int c = 1; c < N; ++c) {
			if (map[r][c] > map[r][c - 1]) {
				if (map[r][c] - map[r][c - 1] > 1) {
					flag = 0;
					break;
				}
				if (L > cnt) {
					flag = 0;
					break;
				}
				cnt = 0;
			}
			else if (map[r][c] < map[r][c - 1]) {
				if (map[r][c - 1] - map[r][c] > 1) {
					flag = 0;
					break;
				}
				if (cnt < 0) {
					flag = 0;
					break;
				}
				cnt = -L;
			}
			++cnt;
		}
		if (flag && cnt >= 0) ++ans;
	}

	// 세로 검사
	for (int c = 0; c < N; ++c) {
		int flag = 1, cnt = 1;
		for (int r = 1; r < N; ++r) {
			if (map[r][c] > map[r - 1][c]) {
				if (map[r][c] - map[r - 1][c] > 1) {
					flag = 0;
					break;
				}
				if (L > cnt) {
					flag = 0;
					break;
				}
				cnt = 0;
			}
			else if (map[r][c] < map[r - 1][c]) {
				if (map[r - 1][c] - map[r][c] > 1) {
					flag = 0;
					break;
				}
				if (cnt < 0) {
					flag = 0;
					break;
				}
				cnt = -L;
			}
			++cnt;
		}
		if (flag && cnt >= 0) ++ans;
	}


	printf("%d", ans);
	return 0;
}