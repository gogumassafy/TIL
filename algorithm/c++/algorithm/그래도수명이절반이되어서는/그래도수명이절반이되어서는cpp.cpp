#include <iostream>
using namespace std;

int T, N, K, W[200000], S[200000] = { 0, }, wearlevel, maxNum, minNum, ans;

bool check(int w) {
	int count = 0, point = 0;
	for (int i = 0; i < N; ++i) {
		if (W[i] > w) {
			count = 0;
			continue;
		}
		++count;
		if (count == S[point]) {
			++point;
			count = 0;
			if (point == K) {
				return true;
			}
		}
	}
	return false;
}

void binary_search(int left, int right) {
	int mid;
	ans = left;
	while (left <= right) {
		mid = (left + right) / 2;
		// 해당 답이 몇인지 고려
		
		if (check(mid)) {
			right = mid - 1;
			ans = mid;
		}
		else {
			left = mid + 1;
		}
	}
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &K);
		minNum = 200000;
		maxNum = 1;
		for (int i = 0; i < N; ++i) {
			scanf("%d", &W[i]);
			if (W[i] > maxNum) {
				maxNum = W[i];
			}
			if (W[i] < minNum) {
				minNum = W[i];
			}
		}
		for (int i = 0; i < K; ++i) {
			scanf("%d", &S[i]);
		}

		binary_search(0, maxNum);
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}

// 이분탐색을 통해 wear level을 정한다.
// 정해진 wear level을 통해서 검사한다.