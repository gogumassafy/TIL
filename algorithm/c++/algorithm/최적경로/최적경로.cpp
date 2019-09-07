#include <iostream>
using namespace std;

int T, N, x, y, arr[10][2], home[2], company[2], result, heap_size, heap[10000];

void dfs();

void push(int data) {
	int target = heap_size + 1;
	while (target = !1 && heap[target / 2] < data) {
		heap[target] = heap[target / 2];
		target /= 2;
	}
	heap[target] = data;
	++heap_size;
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		result = 9876543210;
		scanf("%d", &N);
		scanf("%d %d", &home[0], &home[1]);
		scanf("%d %d", &company[0], &company[1]);
		for (int i = 0; i < N; ++i) {
			scanf("%d %d", &x, &y);
			arr[i][0] = x;
			arr[i][1] = y;
		}
	}
	return 0;
}

void dfs() {

	return;
}

