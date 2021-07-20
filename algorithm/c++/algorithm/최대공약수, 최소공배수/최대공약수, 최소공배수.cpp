#include <iostream>
using namespace std;

int N;
long long input[10];
long long ans[2];

int gcd(int a, int b);

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%lld", &input[i]);
	}
	ans[0] = input[0];
	ans[1] = input[0];
	for (int i = 1; i < N; ++i) {
		ans[0] = gcd(ans[0], input[i]);
		ans[1] = ans[1] * input[i] / gcd(ans[1], input[i]);
	}

	printf("%lld %lld", ans[0], ans[1]);
	return 0;
}

int gcd(int a, int b) {
	int big, small, temp;
	if (a > b) {
		big = a;
		small = b;
	}
	else {
		big = b, small = a;
	}
	temp = big % small;
	while (temp) {
		big = small, small = temp;
		temp = big % small;
	}
	return small;
}