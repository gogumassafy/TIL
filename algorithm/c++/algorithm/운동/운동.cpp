#include <iostream>
#include <string.h>
using namespace std;

int T, N, M, s, e, c, result, arr[401][401], visit[401] = { 0, }, start;


void run(int s, int total);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &M);
		memset(arr, 0, 401);
		result = 987654321;
		for (int m = 0; m < M; ++m) {
			scanf("%d %d %d", &s, &e, &c);
			arr[s][e] = c;
		}
		for (int i = 1; i < N + 1; ++i) {
			start = i;
			run(i, 0);
		}
		if (result == 987654321)
			result = -1;
		printf("#%d %d\n", tc, result);
	}
	return 0;
}

void run(int s, int total) {
	if (total >= result) {
		return;
	}
	if (total && s == start) {
		result = total;
	}
	for (int i = 1; i < N + 1; ++i) {
		if (arr[s][i] == 0)
			continue;
		if (visit[i])
			continue;
		visit[i] = 1;
		run(i, total + arr[s][i]);
		visit[i] = 0;
	}
}