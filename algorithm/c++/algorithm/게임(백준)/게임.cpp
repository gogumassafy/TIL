#include <iostream>
using namespace std;

long long X, Y, Z, ans = -1;

void binarySearch(long long start, long long end);

int main() {
	scanf("%lld %lld", &X, &Y);
	Z = 100 * Y / X;
	if (Z < 99) {
		binarySearch(0, X);
	}
	printf("%lld", ans);
	return 0;
}

void binarySearch(long long start, long long end) {
	long long mid;

	while (start < end) {
		mid = (end + start) / 2;

		if ((100 * (Y + mid) / (X + mid)) > Z) {
			end = mid;
		}
		else {
			start = mid + 1;
		}
	}
	ans = end;
}