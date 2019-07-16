#include <iostream>
using namespace std;

int T, N;
long long leftN, rightN;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		leftN = 1 + (N - 1) * (2 + (N - 2) * 2);
		rightN = 1 + (N - 1) * (6 + (N - 2) * 2);
		leftN = 9223372036854775807;
		printf("#%d %lld %lld\n", tc, leftN, rightN);
	}
	return 0;
}