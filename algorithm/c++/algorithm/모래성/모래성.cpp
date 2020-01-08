#include <iostream>
#include <queue>

using namespace std;

int H, W, time, nr, nc, waveCount, result;
int arr[1000][1000];
int dr[] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dc[] = { -1, 0, 1, -1, 1, -1, 0, 1 };
char chr;

typedef struct point {
	int pr = 0;
	int pc = 0;
} point;

queue<point> q;

int main() {
	scanf("%d %d\n", &H, &W);
	
	for (int r = 0; r < H; ++r) {
		for (int c = 0; c < W; ++c) {
			scanf("%c\n", &chr);
			if (chr == '.') arr[r][c] = 0;
			else arr[r][c] = chr - '0';
		}
	}

	for (int r = 0; r < H; ++r) {
		for (int c = 0; c < W; ++c) {
			waveCount = 0;
			for (int i = 0; i < 8; ++i) {
				nr = dr[i] + r;
				nc = dc[i] + c;
				if (nr < 0 || nc < 0 || nr >= H || nc >= W) continue;
				if (arr[nr][nc] == 0) waveCount++;
			}
			point a = new point;
			if (waveCount >= arr[r][c]) q.push(a);
		}
	}

	while (!q.empty()) {
		time = q.size();
		for (int i = 0; i < time; ++i) {
			q.pop();
		}
	}

	return 0;
}