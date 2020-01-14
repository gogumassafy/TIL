#include <iostream>
using namespace std;

int T, a, b, visited[1000001];
long long phiCount[1000001], phiSum[1000001] = { 0, };

int main() {
	for (int i = 1; i <= 1000000; ++i) {
		phiCount[i] = i;
		visited[i] = 0;
	}

	for (int i = 2; i <= 1000000; ++i) {
		if (visited[i]) continue;
		for (int j = i; j <= 1000000; j += i) {
			phiCount[j] *= i - 1;
			phiCount[j] /= i;
			visited[j] = 1;
		}
	}

	for (int i = 1; i < 1000001; ++i) {
		phiSum[i] += phiSum[i - 1] + phiCount[i];
	}

	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &a, &b);

		printf("#%d %lld\n", tc, phiSum[b] - phiSum[a - 1]);
	}
	return 0;
}