// x값이 >= 49의 제곱근? yes or no로 대답할 수 있게 문제 변환
// yes로 답을 내는 값을 이분탐색을 통해서 가장 작은 애를 찾는다.
// 파라메트릭 서치

#include <iostream>
using namespace std;

int T, N, K, arr[100000], ans, length[100000], length2[100000];

bool check(int W) {
	int count = K;
	for (int i = 0; i < N; ++i) {
		int min = 987654321;
		for (int j = 0; j < N; ++j) {
			int temp = W * (i - j);
			if (temp < 0) {
				temp *= -1;
			}
			temp += arr[j];
			if (temp < min) {
				min = temp;
			}
		}
		count -= (arr[i] - min);
		if (count < 0) {
			return false;
		}
		length[i] = min;
	}
	return true;
}

bool check2(int W) {
	int count = K;
	int min;
	for (int i = 0; i < N; ++i) {
		min = 987654321;
		if (i == 0) {
			min = arr[0];
		}
		else {
			min = length[i - 1] + W;
			if (min > arr[i]) {
				min = arr[i];
			}
		}
		length[i] = min;
	}

	for (int i = N - 1; i >= 0; --i) {
		min = 987654321;
		if (i == N - 1) {
			min = arr[N - 1];
		}
		else {
			min = length2[i + 1] + W;
			if (min > arr[i]) {
				min = arr[i];
			}
		}
		length2[i] = min;
	}

	for (int i = 0; i < N; ++i) {
		min = length[i];
		if (min > length2[i]) {
			min = length2[i];
		}
		count -= arr[i] - min;
		if (count < 0) {
			return false;
		}
	}
	return true;
}

void binarySearch(int left, int right) {
	int mid;
	ans = left;
	while (left <= right) {
		mid = (left + right) / 2;
		if (check2(mid)) {
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
		binarySearch(0, 1000000000);
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}

// 인접한 숫자를 x이하로