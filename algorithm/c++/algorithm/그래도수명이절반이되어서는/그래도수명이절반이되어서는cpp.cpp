#include <iostream>
using namespace std;

int T, N, K, W[200000], visited[200000] = { 0, }, wearlevel;

bool check(int w) {

}

void binary_search(int left, int right) {
	int mid;

	while (left < right) {
		mid = (left + right) / 2;
		// 해당 답이 몇인지 고려
		
		if (check(mid)) {
			left = mid;
		}
		else {
			right = mid;
		}
	}

}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &W[i]);
		}
		binary_search(0, N);
		printf("#%d %d", tc, wearlevel);
	}
	return 0;
}

// 이분탐색을 통해 wear level을 정한다.
// 정해진 wear level을 통해서 검사한다.