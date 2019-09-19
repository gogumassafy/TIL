// x값이 >= 49의 제곱근? yes or no로 대답할 수 있게 문제 변환
// yes로 답을 내는 값을 이분탐색을 통해서 가장 작은 애를 찾는다.
// 파라메트릭 서치

#include <iostream>
using namespace std;

int T, N, K, arr[100000], ans;

bool check(int W) {

}

void binarySearch(int left, int right) {
	int mid;
	ans = left;
	while (left <= right) {
		mid = (left + right) / 2;
		if (check(mid)) {
			ans = mid;
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}
	return;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &arr[i]);
		}
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}

// 인접한 숫자를 x이하로