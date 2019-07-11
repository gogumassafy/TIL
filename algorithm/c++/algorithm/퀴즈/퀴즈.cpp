#include <iostream>
#include <cmath>
using namespace std;

int T, N;
long long arr[1000001] = { 0, }, temp;


long long int power(int number, int up) {
	long long result = 1;
	if (up == 1) {
		return number;
	}
	else {
		result = (power(number, up / 2) % 1000000007);
		result *= result;
		if (up % 2)
			result *= power(number, 1);
	}
	return result % 1000000007;
}

int main() {
	arr[1] = 1;
	for (int i = 2; i < 1000001; ++i) {
		arr[i] = arr[i - 1] + power(i, i);
		arr[i] %= 1000000007;
	}
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		printf("#%d %lld\n", tc, arr[N]);
	}
	return 0;
}