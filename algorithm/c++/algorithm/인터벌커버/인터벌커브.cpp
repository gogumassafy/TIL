#include <iostream>
using namespace std;

long long T, X, N, arr[100][2], S, E, countP;
int comb[100] = { 0, }, minNum, maxNum;

void dfs(int depth);
void calc();

int main() {
	scanf("%ld", &T);
	for (int tc = 1; tc <= T; ++tc) {
		countP = 0;
		scanf("%ld %ld", &X, &N);
		for (int i = 0; i < N; ++i) {
			scanf("%ld %ld", &S, &E);
			arr[i][0] = S;
			arr[i][1] = E;
		}
		dfs(0);
		printf("#%d %ld\n", tc, countP);
	}
	return 0;
}

void dfs(int depth) {
	if (depth == N) {
		minNum = 2;
		maxNum = X - 1;
		calc();
		if (minNum == 1 && maxNum >= X) {
			++countP;
			if (countP >= 1000000007) {
				countP %= 1000000007;
			}
		}
		return;
	}
	comb[depth] = 1;
	dfs(depth + 1);
	comb[depth] = 0;
	dfs(depth + 1);
}

void calc() {
	for (int i = 0; i < N; ++i) {
		if (minNum < arr[i][0]) {
			minNum = arr[i][0];
		}
		if (maxNum > arr[i][1]) {
			maxNum = arr[i][1];
		}
	}
}