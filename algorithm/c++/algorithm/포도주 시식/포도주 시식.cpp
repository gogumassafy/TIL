#include <iostream>
using namespace std;

<<<<<<< HEAD
int N, wine[10000];
=======
int N, wine[10000], visited[10000], ans = 0, sumWine[10000];

void dfs(int depth, int sum, int cnt);

void dp();
>>>>>>> e42dc078a167e686ed57a8c0f1a0888918224972

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &wine[i]);
	}

<<<<<<< HEAD


	return 0;
=======
	dp();

	printf("%d", sumWine[N - 1]);
	return 0;
}

void dfs(int depth, int sum, int cnt) {
	if (sum > ans) ans = sum;

	for (int i = depth; i < N; ++i) {
		if (i >= 2) {
			if (cnt >= 2) {
				cnt -= visited[i - 2];
				continue;
			}
			cnt -= visited[i - 2];
		}
		visited[i] = 1;
		cnt += visited[i];
		dfs(i + 1, sum + wine[i], cnt);
		cnt -= visited[i];
		visited[i] = 0;
	}
}

void dp() {
	sumWine[0] = wine[0];
	sumWine[1] = sumWine[0] + wine[1];
	sumWine[2] = sumWine[0] + wine[2] > wine[1] + wine[2] ? sumWine[0] + wine[2] : wine[1] + wine[2];

	for (int i = 1; i < N; ++i) {
		sumWine[i] = sumWine[i - 2] + wine[i] > sumWine[i - 3] + wine[i - 1] + wine[i] ? sumWine[i - 2] + wine[i] : sumWine[i - 3] + wine[i - 1] + wine[i];
		sumWine[i] = sumWine[i - 1] > sumWine[i] ? sumWine[i - 1] : sumWine[i];
		
	}
>>>>>>> e42dc078a167e686ed57a8c0f1a0888918224972
}