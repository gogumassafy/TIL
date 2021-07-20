#include <iostream>
using namespace std;

int N, M, X, Y, Z, input[101][101], ans[101] = { 0, }, partInfo[101];

void calc(int partNum, int makeCnt);

int main() {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; ++i) {
		scanf("%d %d %d", &X, &Y, &Z);
		input[X][Y] = Z;
		partInfo[X] = 1;
	}

	calc(N, 1);

	for (int i = 1; i < N; ++i) {
		if (partInfo[i]) continue;
		printf("%d %d\n", i, ans[i]);
	}
	return 0;
}

void calc(int partNum, int makeCnt) {
	if (partInfo[partNum]) {
		for (int i = 1; i < N; ++i) {
			if (input[partNum][i] == 0) continue;
			calc(i, makeCnt * input[partNum][i]);
		}
	}
	else {
		ans[partNum] += makeCnt;
	}
}