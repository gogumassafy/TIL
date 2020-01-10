#include <iostream>
using namespace std;

#define MAX_SIZE 100000

int N, M, K;
int input[1000][1000], visited[1000][1000][11];
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

typedef struct {
	int length;
	int r;
	int c;
	int bomb;
} Point;

Point heap[MAX_SIZE];
int heapSize = 0;

void heapInit(void) {
	heapSize = 0;
}

int heapPush(Point value) {
	/* * /if (heapSize + 1 > MAX_SIZE) {
		// full
		printf("it's full\n");
		return 0;
	 } /* */
	
	heap[heapSize] = value;
	int current = heapSize;

	while (current > 0 && heap[current].length < heap[(current - 1) / 2].length) {
		Point temp = heap[(current - 1) / 2];
		heap[(current - 1) / 2] = heap[current];
		heap[current] = temp;
		current = (current - 1) / 2;
	}

	heapSize = heapSize + 1;

	return 1;
}

int heapPop(Point *value) {
	if (heapSize <= 0) {
		return -1;
	}

	*value = heap[0];
	--heapSize;

	heap[0] = heap[heapSize];

	int current = 0;
	while (current * 2 + 1 < heapSize){
		int child;
		if (current * 2 + 2 == heapSize) {
			child = current * 2 + 1;
		}
		else {
			child = heap[current * 2 + 1].length < heap[current * 2 + 2].length ? current * 2 + 1 : current * 2 + 2;
		}

		if (heap[current].length < heap[child].length) break;

		Point temp = heap[current];
		heap[current] = heap[child];
		heap[child] = temp;

		current = child;
	}
	return 1;
}


int bfs();

int main() {
	scanf("%d %d %d", &N, &M, &K);
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf("%1d", &input[r][c]);
		}
	}
	Point start = { 1, 0, 0 , K};
	heapPush(start);
	visited[0][0][K] = 1;
	printf("%d", bfs());
	return 0;
}

int bfs() {
	Point p, next;
	while (heapSize) {
		heapPop(&p);
		if (p.r == (N - 1) && p.c == (M - 1)) return p.length;
		for (int d = 0; d < 4; ++d) {
			int nr = p.r + dr[d];
			int nc = p.c + dc[d];
			if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
			if (visited[nr][nc][p.bomb]) continue;
			if (input[nr][nc]) {
				if (p.bomb < 1) continue;
				else {
					next = {p.length + 1, nr, nc, p.bomb - 1};
					heapPush(next);
				}
			}
			else {
				next = { p.length + 1, nr, nc, p.bomb };
				heapPush(next);
			}
			visited[nr][nc][next.bomb] = 1;
		}
	}
	return -1;
}