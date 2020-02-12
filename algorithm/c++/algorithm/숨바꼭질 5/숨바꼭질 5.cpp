#include <iostream>
using namespace std;

#define MAX_N 10000

int queue[MAX_N];
int front, rear;

int N, K, visited[500000];

void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(int value);
int queueDeque(int* value);

int main() {
	scanf("%d %d", &N, &K);


}