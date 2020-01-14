#include <iostream>
using namespace std;

int T, N;
long long input[1000000], sort[1000000], ans;

long long dq(int start, int end);

int main() {
	ans = 0;
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%lld", &input[i]);
		sort[i] = input[i];
	}

	ans = dq(0, N - 1);
	printf("%lld\n", ans);

	return 0;
}

long long dq(int start, int end) {
	long long mid = (start + end) / 2, left = start, right = mid + 1, value = 0, temp = 0, counting = start;
	if (start == end) return 0;
	value = dq(start, mid) + dq(mid + 1, end);
	while (left <= mid && right <= end) {
		if (input[left] < input[right]) {
			sort[counting++] = input[left++];
			value += temp;
		}
		else {
			sort[counting++] = input[right++];
			++temp;
		}
	}

	while (left <= mid) {
		sort[counting++] = input[left++];
		value += temp;
	}
	while (right <= end) {
		sort[counting++] = input[right++];
	}

	for (int i = start; i <= end; ++i) {
		input[i] = sort[i];
	}

	return value;
}