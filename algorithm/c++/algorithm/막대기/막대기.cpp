#include <iostream>
using namespace std;

int X, N = 64, ans = 0;

int main() {
	scanf("%d", &X);

	while (X) {
		if (X >= N) {
			X -= N;
			++ans;
		}
		else {
			N >>= 1;
		}
	}

	printf("%d\n", ans);

	return 0;
}