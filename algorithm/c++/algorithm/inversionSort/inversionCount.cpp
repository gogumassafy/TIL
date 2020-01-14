#include <iostream>
using namespace std;

int T, N, input[100000], sort[100000], ans;

int dq(int start, int end);

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		ans = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &input[i]);
			sort[i] = input[i];
		}

		ans = dq(0, N - 1);
		printf("#%d %d", tc, ans);
	}
	return 0;
}

int dq(int start, int end) {
	int mid = (start + end) / 2, left = start, right = mid + 1, value = 0, temp = 0, counting = start;
	if (start == end) return 0;
	value = dq(start, mid) + dq(mid + 1, end);
	while (left <= mid && right <= end) {
		if (input[left] <= input[right]) {
			// 새로운 배열에 뽑아주고 left 1증가
			sort[counting++] = input[left];
			value += temp;

		}
		else {
			// 새로운 배열에 뽑아주고 right 1증가
			sort[counting++] = input[right];
			++temp;
		}
	}

	for (int i = start; i <= end; ++i) {
		input[i] = sort[i];
	}

	return value;
}