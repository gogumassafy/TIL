#include <iostream>
using namespace std;

int way[100][100], visited[100] = { 0, }, queue[100];
int ans, T, N, start, goal, front, rear, now, next;

void queueInit(void) {
	front = 0;
	rear = 0;
}

int queueIsEmpty(void) {
	return (front == rear);
}

int queueIsFull(void) {
	if ((rear + 1) % 100 == front) {
		return 1;
	}
	else {
		return 0;
	}
}

int queueEnqueue(int value) {
	if (queueIsFull()) {
		return 0;
	}
	queue[rear++] = value;
	if (rear == 100) {
		rear = 0;
	}
	return 1;
}

int queueDequeue(int *value) {
	if (queueIsEmpty()) {
		return 0;
	}
	*value = queue[front++];
	if (front == 100) {
		front = 0;
	}
	return 1;
}

int bfs() {
	while (!queueIsEmpty()) {
		queueDequeue(&now);
		if (now == 99) return 1;
		for (int i = 0; i < 100; ++i) {
			if (way[now][i] == 0) continue;
			if (visited[i]) continue;
			queueEnqueue(i);
			visited[i] = 1;
		}
	}
	return 0;
}

int main() {
	for (int tc = 1; tc <= 10; ++tc) {
		for (int r = 0; r < 100; ++r) {
			visited[r] = 0;
			for (int c = 0; c < 100; ++c) {
				way[r][c] = 0;
			}
		}
		ans = 0;
		scanf("%d %d", &T, &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d %d", &start, &goal);
			way[start][goal] = 1;
		}
		queueInit();
		queueEnqueue(0);
		visited[0] = 1;
		ans = bfs();
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}