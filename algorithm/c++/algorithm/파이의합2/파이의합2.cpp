// indexed tree를 사용하여 문제를 풀 예정
#include <iostream>
using namespace std;

#define MAX_N 1000001
#define base 1<<20

int T, a, b, visited[MAX_N];
unsigned long long ans;
unsigned long long phi[MAX_N], sumPhi[1 << 21] = { 0, };

unsigned long long getValue(int start, int end);

int main() {
	for (int i = 1; i < MAX_N; ++i) {
		phi[i] = i;
		visited[i] = 0;
	}

	for (int i = 2; i < MAX_N; ++i) {
		if (visited[i] == 1) continue;
		for (int j = i; j < MAX_N; j += i) {
			phi[j] *= (unsigned long long) i - 1;
			phi[j] /= i;
			visited[j] = 1;
		}
	}

	for (int i = 1; i < MAX_N; ++i) {
		sumPhi[1048575 + i] = phi[i];
	}

	int idx = base;

	while (idx) {
		for (int start = idx >> 1; start < idx; ++start) {
			sumPhi[start] = sumPhi[start * 2] + sumPhi[start * 2 + 1];
		}
		idx /= 2;
	}

	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		ans = 0;
		scanf("%d %d", &a, &b);
		ans = getValue(a, b);
		printf("#%d %llu\n", tc, ans);
	}
	return 0;
}

unsigned long long getValue(int start, int end) {
	int left = (base) + start - 1, right = (base) + end - 1;
	unsigned long long value = 0;
	while (left <= right) {
		if (left % 2) {
			value += sumPhi[left++];
		}
		if (right % 2 == 0) {
			value += sumPhi[right--];
		}

		left /= 2;
		right /= 2;
	}

	return value;
}