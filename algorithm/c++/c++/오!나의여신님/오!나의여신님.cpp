#include <stdio.h>
#include <deque>
#include <string.h>

using namespace std;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int T, N, M, visited[50][50], arr[50][50], sr, sc, der, dec, nr, nc, solution;
struct rc {
	int r, c;
};
deque<rc> su;
deque<rc> devil;


int bfs() {
	int qLen;
	while (1) {
        if (su.empty())
		{
			return 0;
		}
		qLen = devil.size();
		while (qLen--) {
			der = devil.front().r;
			dec = devil.front().c;
			devil.pop_front();
			for (int i = 0; i < 4; ++i) {
				nr = der + dr[i];
				nc = dec + dc[i];
				if (nr >= N || nc >= M || nr < 0 || nc < 0)
					continue;
				if (arr[nr][nc] < 0)
					continue;
				rc next;
				next.r = nr;
				next.c = nc;
				devil.push_back(next);
				arr[nr][nc] = -1;
			}
		}
		qLen = su.size();
		while (qLen--) {
			sr = su.front().r;
			sc = su.front().c;
			su.pop_front();
			for (int i = 0; i < 4; ++i) {
				nr = sr + dr[i];
				nc = sc + dc[i];
				if (nr >= N || nc >= M || nr < 0 || nc < 0)
					continue;
				if (visited[nr][nc])
					continue;
				if (arr[nr][nc] == -1 || arr[nr][nc] == -3)
					continue;
				if (arr[nr][nc] == -2)
					return visited[sr][sc];
				rc next;
				next.r = nr;
				next.c = nc;
				su.push_back(next);
				visited[nr][nc] = visited[sr][sc] + 1;
			}
		}
	}
	return 0;
}


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d %d", &N, &M);
		memset(visited, 0, sizeof(visited));
		memset(arr, 0, sizeof(arr));
		for (int r = 0; r < N; ++r) {
			for (int c = 0; c < M; ++c) {
				char ch;
				scanf(" %c", &ch);
				rc temp;
				temp.r = r;
				temp.c = c;
				if (ch == '.')
					continue;
				else if (ch == 'S') {
					su.push_back(temp);
					visited[r][c] = 1;
					arr[r][c] = 1;

				}
				else if (ch == '*') {
					devil.push_back(temp);
					arr[r][c] = -1;
				}
				else if (ch == 'X') {
					arr[r][c] = -3;
				}
				else if (ch == 'D') {
					arr[r][c] = -2;
				}
					
			}
		}
		solution = bfs();
		if (solution) {
			printf("#%d %d\n", tc, solution);
		}
		else {
			printf("#%d GAME OVER\n", tc);
		}
		su.clear();
		devil.clear();
	}
	return 0;
}