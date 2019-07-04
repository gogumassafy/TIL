#include <stdio.h>
#include <string.h>
#include <deque>
using namespace std;


int T, N, arr[100][100], maxN = 0, minN = 100;
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };


void bfs() {

}


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &arr[i][j]);
				if (minN > arr[i][j])
					minN = arr[i][j];
				if (maxN < arr[i][j])
					maxN = arr[i][j];
			}
		}
		int result = 1;
		int visited[100][100];
		for (int i = minN; i < maxN; ++i) {
			memset(visited, 0, sizeof(visited));
			int count = 0;
			for (int r = 0; r < N; ++r) {
				for (int c = 0; c < N; ++c) {
					deque<pair<int, int>> dq;
					if (arr[r][c] <= i)
						continue;
					if (visited[r][c])
						continue;
					count++;
					dq.push_back(make_pair(r, c));
					while (!dq.empty()) {
						int sr = dq.front().first;
						int sc = dq.front().second;
						dq.pop_front();
						for (int j = 0; j < 4; ++j) {
							int nr = sr + dr[j];
							int nc = sc + dc[j];
							if (nr == N || nc == N || nr < 0 || nc < 0)
								continue;
							if (visited[nr][nc])
								continue;
							if (arr[nr][nc] <= i)
								continue;
							dq.push_back(make_pair(nr, nc));
							visited[nr][nc] = count;
						}
					}
				}
			}
			if (count > result)
				result = count;
		}
		printf("#%d %d\n", tc, result);
	}
	return 0;
}