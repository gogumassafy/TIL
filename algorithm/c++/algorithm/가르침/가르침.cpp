#include <iostream>
using namespace std;

int N, K, ans = 0, visited[26], selected[26];
char input[50][16], base[] = "antic";

void dfs(int depth, int k);
void check();

int main() {
	scanf("%d %d\n", &N, &K);
	for (int i = 0; i < N; ++i) {
		int idx = 0;
		while (scanf("%c", &input[i][idx])) {
			if (input[i][idx] == '\n') {
				input[i][idx] = '\0';
				break;
			}
			else {
				visited[input[i][idx] - 'a'] = 1;
			}
			++idx;
		}
	}
	if (K < 5) {
		printf("%d\n", ans);
		return 0;
	}
	// a, n, t, i, c´Â ÇÊ¼ö
	int idx;
	for (int i = 0; i < 5; ++i) {
		idx = base[i] - 'a';
		selected[idx] = 1;
	}

	dfs(5, 0);

	printf("%d\n", ans);
	return 0;
}

void dfs(int depth, int k) {
	if (depth == K) {
		check();
		return;
	}

	for (int i = k; i < 26; ++i) {
		if (visited[i] == 0) continue;
		if (selected[i]) continue;

		selected[i] = 1;
		dfs(depth + 1, i + 1);
		selected[i] = 0;
	}
	check();
}

void check() {
	const char* str;
	int c, flag, temp = 0;
	for (int i = 0; i < N; ++i) {
		str = input[i];
		flag = 1;
		while (c = *str++) {
			if (selected[c - 'a'] == 0) {
				flag = 0;
				break;
			}
		}
		if (flag) {
			++temp;
		};
	}
	if (temp > ans) ans = temp;
}