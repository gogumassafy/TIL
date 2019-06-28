#include <stdio.h>

int T, N, M, result;
int arr[750][750];
int dr[] = { 1, 1, 1, 1 };
int dc[] = { -1, 1, 1, -1 };


void run(int r, int c) {
	int lr = r, lc = c, rr = r, rc = c, count = 0;
	int dlr, dlc, drr, drc, flag;

	if (result > c || result > (M - c - 1) || 2*result > (N - r)) {
		return;
	}

	while (1) {
		count += 1;
		if (count > result) {
			dlr = lr, dlc = lc;
			drr = rr, drc = rc;
			flag = 1;
			for (int i = 0; i < count - 1; ++i) {
				dlr += dr[2];
				dlc += dc[2];
				drr += dr[3];
				drc += dc[3];
				if (dlr >= N || drr >= N) {
					flag = 0;
					break;
				}
				if (arr[dlr][dlc] == 0 || arr[drr][drc] == 0) {
					flag = 0;
					break;
				}
			}
			if (flag) {
				result = count;
			}
		}
		lr += dr[0];
		lc += dc[0];
		rr += dr[1];
		rc += dc[1];
		if (lr >= N || rr >= N || lc < 0 || rc >= M) {
			return;
		}
		if (arr[lr][lc] == 0 || arr[rr][rc] == 0) {
			return;
		}
	}
	return;
}


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		result = 0;
		scanf("%d %d", &N, &M);
		for (int r = 0; r < N; ++r) {
			for (int c = 0; c < M; ++c) {
				scanf("%1d", &arr[r][c]);
			}
		}
		for (int r = 0; r < N; ++r) {
			for (int c = 0; c < M; ++c) {
				if (arr[r][c]) {
					run(r, c);
				}
			}
		}
		printf("#%d %d\n", tc, result);
	}
	return 0;
}