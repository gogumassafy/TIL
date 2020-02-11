#include <iostream>
using namespace std;

#define MAX_N 2501

typedef struct _Point {
	int r;
	int c;

	_Point() {
		r = 0;
		c = 0;
	}

	_Point(int _r, int _c) {
		r = _r;
		c = _c;
	}
} Point;


int N, M, map[50][50], totalRoom = 0, maxRoomCnt = 0, sumCnt = 0;

int main() {
	scanf("%d %d", &N, &M);
	for (int r = 0; r < M; ++r) {
		for (int c = 0; c < N; ++c) {
			scanf("%d", &map[r][c]);
		}
	}
	return 0;
}