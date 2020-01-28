#include <iostream>
using namespace  std;

// го ©Л ╩С аб
int dr[4] = { 1, 0, -1, 0 };
int dc[4] = { 0, 1, 0, -1 };

int L;
char input[50], map[101][101];

int main() {
	for (int r = 0; r < 101; ++r) {
		for (int c = 0; c < 101; ++c) {
			map[r][c] = '#';
		}
	}
	int sr = 50, sc = 50, er = 51, ec = 51, d = 0, nr = 50, nc = 50;
	char temp;
	map[nr][nc] = '.';
	scanf("%d", &L);
	for (int i = 0; i < L; ++i) {
		scanf(" %c", &temp);
		if (temp == 'R') d = (d + 3) % 4;
		else if (temp == 'L') d = (d + 1) % 4;
		else {
			nr += dr[d];
			nc += dc[d];
			map[nr][nc] = '.';
			if (nr < sr) sr = nr;
			else if (nr == er) ++er;
			if (nc < sc) sc = nc;
			else if (nc == ec) ++ec;
		}
	}
	
	for (int i = sr; i < er; ++i) {
		for (int j = sc; j < ec; ++j) {
			printf("%c", map[i][j]);
		}
		printf("\n");
	}
	return 0;
}