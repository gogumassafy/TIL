#include <iostream>
using namespace std;

#define MAX_N 1000

typedef struct _Water {
	int store[3];

	_Water() {
		for (int i = 0; i < 3; ++i) {
			store[i] = 0;
		}
	}

	_Water(int _a, int _b, int _c) {
		store[0] = _a;
		store[1] = _b;
		store[2] = _c;
	}

	_Water(int input[]) {
		for (int i = 0; i < 3; ++i) {
			store[i] = input[i];
		}
	}

	_Water(_Water* w) {
		for (int i = 0; i < 3; ++i) {
			store[i] = w->store[i];
		}
	}
} Water;

Water queue[MAX_N];
int front, rear;

int base[3], visited[200][200][200], ans[200];

void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Water w);
int queueDeque(Water* w);
void bfs();

int main() {
	for (int i = 0; i < 3; ++i) {
		scanf("%d", &base[i]);
	}
	queuePush(Water(0, 0, base[2]));
	visited[0][0][base[2]] = 1;
	ans[base[2]] = 1;
	bfs();

	for (int i = 0; i <= base[2]; ++i) {
		if (ans[i]) printf("%d ", i);
	}
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

int queuePush(Water w) {
	if (queueIsFull()) return 0;

	queue[rear++] = w;
	if (rear == MAX_N) rear = 0;
	return 1;
}

int queueDeque(Water* w) {
	if (queueIsEmpty()) return 0;

	*w = queue[front++];
	if (front == MAX_N) front = 0;
	return 1;
}

void bfs() {
	Water now;
	while (!queueIsEmpty()) {
		queueDeque(&now);
		
		for (int i = 0; i < 3; ++i) {
			if (now.store[i] == 0) continue;
			for (int j = 1; j <= 2; ++j) {
				Water next(now);
				int d = (i + j) % 3;
				if (next.store[d] == base[d]) continue;

				int howMuch = base[d] - next.store[d];
				if (howMuch > next.store[i]) howMuch = next.store[i];

				next.store[d] += howMuch;
				next.store[i] -= howMuch;

				if (visited[next.store[0]][next.store[1]][next.store[2]]) continue;
				visited[next.store[0]][next.store[1]][next.store[2]] = 1;
				if (next.store[0] == 0) ans[next.store[2]] = 1;
				queuePush(next);
			}
		}
	}
}