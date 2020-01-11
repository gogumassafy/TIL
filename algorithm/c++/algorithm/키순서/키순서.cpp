#include <iostream>
using namespace std;

#define INF 987654321

int T, ans, N, M, a, b;
int d[501][501];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		ans = 0;
		for (int i = 1; i <= 500; ++i) {
			for (int j = 1; j <= 500; ++j) {
				d[i][j] = INF;
			}
		}
		scanf("%d %d", &N, &M);
		for (int i = 0; i < M; ++i) {
			scanf("%d %d", &a, &b);
			d[a][b] = 1;
		}

		for (int k = 1; k <= N; ++k) {
			for (int s = 1; s <= N; ++s) {
				for (int e = 1; e <= N; ++e) {
					if (d[s][e] > (d[s][k] + d[k][e])) {
						d[s][e] = d[s][k] + d[k][e];
					}
				}
			}
		}

		for (int i = 1; i <= N; ++i) {
			int flag = 1;
			for (int j = 1; j <= N; ++j) {
				if (i == j || d[i][j] < INF || d[j][i] < INF) continue;
				flag = 0;
			}
			if (flag) ++ans;
		}

		printf("#%d %d\n", tc, ans);
	}
	return 0;
}