#include <iostream>
#include <string.h>
using namespace std;

int T, R, C, visit[4][16][20][20] = { 0, }, result, memory;
// »óÇÏÁÂ¿ì
int dr[4] = { -1, 1, 0, 0 }, dc[4] = { 0, 0, -1, 1 };
char arr[20][20];

void dfs(int dir, int sr, int sc);

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		result = 0;
		memory = 0;
		memset(visit, 0, sizeof(visit));
		scanf("%d %d", &R, &C);
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				scanf(" %c", &arr[r][c]);
			}
		}
		dfs(3, 0, -1);
		if (result) {
			printf("#%d YES\n", tc);
		}
		else {
			printf("#%d NO\n", tc);
		}
	}
	return 0;
}


void dfs(int dir, int sr, int sc) {
	if (result) {
		return;
	}
	int nr, nc;
	nr = sr + dr[dir];
	nc = sc + dc[dir];
	if (nr == R) {
		nr = 0;
	}
	else if (nr == -1) {
		nr = R - 1;
	}
	else if (nc == C) {
		nc = 0;
	}
	else if (nc == -1) {
		nc = C - 1;
	}
	if (visit[dir][memory][nr][nc]) {
		return;
	}
	if (arr[nr][nc] == '<') {
		visit[dir][memory][nr][nc] = 1;
		dfs(2, nr, nc);
	}
	else if (arr[nr][nc] == '>') {
		visit[dir][memory][nr][nc] = 1;
		dfs(3, nr, nc);
	}
	else if (arr[nr][nc] == '^') {
		visit[dir][memory][nr][nc] = 1;
		dfs(0, nr, nc);
	}
	else if (arr[nr][nc] == 'v') {
		visit[dir][memory][nr][nc] = 1;
		dfs(1, nr, nc);
	}
	else if (arr[nr][nc] == '_') {
		visit[dir][memory][nr][nc] = 1;
		if (memory == 0) {
			dfs(3, nr, nc);
		}
		else {
			dfs(2, nr, nc);
		}
	}
	else if (arr[nr][nc] == '|') {
		visit[dir][memory][nr][nc] = 1;
		if (memory == 0) {
			dfs(1, nr, nc);
		}
		else {
			dfs(0, nr, nc);
		}
	}
	else if (arr[nr][nc] == '?') {
		for (int i = 0; i < 4; ++i) {
			visit[i][memory][nr][nc] = 1;
		}
		for (int i = 0; i < 4; ++i) {
			dfs(i, nr, nc);
		}
	}
	else if (arr[nr][nc] == '.') {
		visit[dir][memory][nr][nc] = 1;
		dfs(dir, nr, nc);
	}
	else if (arr[nr][nc] == '@') {
		visit[dir][memory][nr][nc] = 1;
		result = 1;
		return;
	}
	else if (arr[nr][nc] >= '0' && arr[nr][nc] <= '9') {
		for (int i = 0; i < 16; ++i) {
			visit[dir][i][nr][nc] = 1;
		}
		memory = arr[nr][nc] - '0';
		dfs(dir, nr, nc);
	}
	else if (arr[nr][nc] == '+') {
		visit[dir][memory][nr][nc] = 1;
		memory++;
		if (memory > 15) {
			memory = 0;
		}
		dfs(dir, nr, nc);
	}
	else if (arr[nr][nc] == '-') {
		visit[dir][memory][nr][nc] = 1;
		memory--;
		if (memory < 0) {
			memory = 15;
		}
		dfs(dir, nr, nc);
	}
	return;
}