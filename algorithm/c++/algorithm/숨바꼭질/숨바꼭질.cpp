#include <iostream>
using namespace std;

#define MAX_N 100001

int front, rear;
int queue[MAX_N];

void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(int value);
int queueDeque(int* value);

void bfs();

int N, K, ans;
int visited[MAX_N];

int main() {
	scanf("%d %d", &N, &K);
	
	bfs();

	printf("%d", ans);
	return 0;
}

void queueInit() {
	front = 0;
	rear = 0;
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
	int now, t, time = 0;
	visited[N] = 1;
	queuePush(N);
	while (!queueIsEmpty()) {
		t = (rear - front + MAX_N) % MAX_N;
		while (t--) {
			queueDeque(&now);
			if (now == K) {
				ans = time;
				return;
			}
			
			for (int i = 0; i < 3; ++i) {
				int next = now;
				if (i == 0) next += 1;
				else if (i == 1) next -= 1;
				else next *= 2;
				if (next < 0 || next >= MAX_N) continue;
				if (visited[next]) continue;
				visited[next] = 1;
				queuePush(next);
			}
		}
		++time;
	}
}