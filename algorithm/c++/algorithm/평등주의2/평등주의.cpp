#include <iostream>
using namespace std;

int T, N, K, ans, maxNum, cutCount, temp;
int input[100000], leftToRight[100000], rightToLeft[100000];

int binarySearch(int first, int end);

int isAvailable(int mid);

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		maxNum = 0;
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &input[i]);
			if (input[i] > maxNum) maxNum = input[i];
		}
		ans = binarySearch(0, maxNum);
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}

int binarySearch(int first, int end) {
	int mid;

	while (first < end) {
		mid = (first + end) / 2;
		if (isAvailable(mid)) {
			end = mid;
		}
		else {
			first = mid + 1;
		}
	}
	return end;
}

int isAvailable(int mid) {
	// 가능하면 return 1;
	// 가능하면 return 0;

	cutCount = 0;

	for (int i = 0; i < N; ++i) {
		if (i == 0 || input[i] < leftToRight[i - 1] + mid) {
			leftToRight[i] = input[i];
		}
		else {
			leftToRight[i] = leftToRight[i - 1] + mid;
		}

		if (i == 0 || input[(N - 1) - i] < rightToLeft[N - i] + mid) {
			rightToLeft[(N - 1) - i] = input[(N - 1) - i];
		}
		else {
			rightToLeft[(N - 1) - i] = rightToLeft[N - i] + mid;
		}
		
	}

	for (int i = 0; i < N; ++i) {
		if (leftToRight[i] >= rightToLeft[i]) {
			cutCount += input[i] - rightToLeft[i];
		}
		else {
			cutCount += input[i] - leftToRight[i];
		}
		if (cutCount > K) return 0;
	}
	return 1;
}