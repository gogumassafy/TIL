#include <iostream>
using namespace std;

int N, K, I, ans = -1;

int merge(int left, int right, int cnt);

int main() {
	int count = 0, temp;
	scanf("%d %d %d", &N, &K, &I);
	temp = 1;
	while (N > temp) {
		temp <<= 1;
		++count;
	}
	merge(1, temp, count);
	return 0;
}

int merge(int left, int right, int cnt) {
	if (right - left == 0) return left;

	int mid, newLeft, newRight;

	if ((right - left) % 2) {
		mid = (left + right) / 2;

		newLeft = merge(left, mid, cnt - 1);
		newRight = merge(mid + 1, right, cnt - 1);
	}
	else {
		newLeft = merge(left, right - 1, cnt - 1);
		newRight = right;
	}
	
	if (newRight == K || newRight == I) {
		if (newLeft == K && newRight == I || newRight == K && newLeft == I) {
			ans = cnt;
			printf("%d\n", ans);
		}
		return newRight;
	}

	return newLeft;
}