#include <stdio.h>
#include <vector>
using namespace std;

int T, result, N, M;
long long treeHeight[1000001], endHeight, startHeight, mid, sum;


int search(int goal);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		endHeight = 0;
		startHeight = 1e9;
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; ++i) {
			scanf("%lld", &treeHeight[i]);
			if (treeHeight[i] > endHeight) {
				endHeight = treeHeight[i];
			}
			if (treeHeight[i] < startHeight) {
				startHeight = treeHeight[i];
			}
		}
		result = search(M);
		printf("#%d %d\n", tc, result);
	}
	return 0;
}


int search(int goal) {
	while (startHeight <= endHeight) {
		sum = 0;
		mid = (startHeight + endHeight) / 2;
		for (int i = 0; i < N; ++i) {
			if (treeHeight[i] > mid) {
				sum += treeHeight[i] - mid;
			}
		}
		if (sum >= goal) {
			startHeight = mid + 1;
		}
		else {
			endHeight = mid - 1;
		}
	}
	return endHeight;
}