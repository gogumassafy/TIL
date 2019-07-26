#include <iostream>
using namespace std;


int T, R, C, result;
char arr[20][20];


void bfs();


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		result = 0;
		scanf("%d %d", &R, &C);
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				scanf("%c", &arr[r][c]);
			}
		}
		for (int i = 0; i < R; ++i) {
			for (int k = 0; k < C; ++k) {

			}
		}
	}
	return 0;
}

void bfs() {
	return;
}
