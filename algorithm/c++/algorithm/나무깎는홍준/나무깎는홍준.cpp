#include <stdio.h>
#include <vector>
using namespace std;

int T, treeHeight[1000000], result, endHeight, sum, mid, startHeight, N, M;


int search(int goal);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		endHeight = 0;
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &treeHeight[i]);
			if (treeHeight[i] > endHeight) {
				endHeight = treeHeight[i];
			}
		}
		result = search(M);
		printf("#%d %d\n", tc, result);
	}
	return 0;
}


int search(int goal) {
	startHeight = 0;

	while (startHeight < endHeight) {
		sum = 0;
		mid = (startHeight + endHeight) / 2;
		for (int i = 0; i < N; ++i) {
			if (treeHeight[i] > mid) {
				sum += treeHeight[i] - mid;
			}
		}
		if (sum == goal) {
			return mid;
		}
		else if (sum > goal) {
			startHeight = mid + 1;
		}
		else {
			endHeight = mid;
		}
	}
	return endHeight;
}