#include <iostream>
using namespace std;

int T, N, M;
long long ans, countNum[31][31];

void dp();

int main() {
	scanf("%d", &T);
	dp();
	for (int tc = 0; tc < T; ++tc) {
		ans = 0;
		scanf("%d %d", &N, &M);
		printf("%lld\n", countNum[N][M]);
	}
	return 0;
}

void dp() {
	for (int n = 1; n <= 30; ++n) {
		for (int m = 1; m <= 30; ++m) {
			if (n == 1) countNum[n][m] = m;
			else {
				for (int k = 1; k < m; ++k) {
					countNum[n][m] += countNum[n - 1][m - k];
				}
			}
		}
	}

}