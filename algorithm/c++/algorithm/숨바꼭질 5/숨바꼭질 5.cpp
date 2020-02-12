#include <iostream>
using namespace std;

#define MAX_N 100002

int queue[MAX_N];
int front, rear;

int N, K, visited[2][500001];

void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(int value);
int queueDeque(int* value);
void bfs();

int main() {
	scanf("%d %d", &N, &K);
	queueInit();
	queuePush(N);
	bfs();
	return 0;
}

void queueInit() {
	front = 0;
	rear = 0;
	return;
}

int queueIsEmpty() {
	return front == rear;
}

int queueIsFull() {
	return (rear + 1) % MAX_N == front;
}

int queuePush(int value) {
	if (queueIsFull()) return 0;

	queue[rear++] = value;
	if (rear == MAX_N) rear = 0;
	return 1;
}

int queueDeque(int* value) {
	if (queueIsEmpty()) return 0;

	*value = queue[front++];
	if (front == MAX_N) front = 0;
	return 1;
}

void bfs() {
	int time = 1, now, next, oneTime;
	while (!queueIsEmpty()) {
		oneTime = (rear - front + MAX_N) % MAX_N;

		while (oneTime--) {
			queueDeque(&now);
			if (now == K) {
				printf("%d", time - 1);
				return;
			}
			for (int d = 0; d < 3; ++d) {
				if (d == 0) next = now - 1;
				else if (d == 1) next = now + 1;
				else next = now << 1;

				if (next < 0 || next > 500000) continue;
				if (visited[time % 2][next]) continue;
				
				visited[time % 2][next] = time;
				queuePush(next);
			}
		}

		K += time;
		if (K > 500000) {
			printf("-1\n");
			return;
		}
		if (visited[time % 2][K]) {
			printf("%d\n", time);
			return;
		}
		++time;
	}
}