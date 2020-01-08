#include <iostream>
using namespace std;

int T, N, K, ans, minNum, maxNum, countK, numsOfBlock;
int input[200000], block[200000];

int countBlock(int value) {
	countK = 0;
	numsOfBlock = 0;
	// return 1은 가능한 경우
	// return 0는 불가능한 경우
	for (int i = 0; i < N; ++i) {
		if (input[i] <= value) ++numsOfBlock;
		else if (numsOfBlock > 0) numsOfBlock = 0;
		if (block[countK] == numsOfBlock) {
			++countK;
			numsOfBlock = 0;
		}
		if (countK == K) return 1;
	}
	return 0;
}

int binarySearch(int first, int end) {
	int mid;

	while (first < end) {
		mid = (first + end) / 2;
		if (countBlock(mid)) {
			end = mid;
		}
		else {
			first = mid + 1;
		}
	}
	return end;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		ans = 987654321;
		minNum = 987654321;
		maxNum = 0;

		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &input[i]);
			if (maxNum < input[i]) maxNum = input[i];
			if (minNum > input[i]) minNum = input[i];
		}
		for (int i = 0; i < K; ++i) {
			scanf("%d", &block[i]);
		}
		ans = binarySearch(minNum, maxNum);
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}