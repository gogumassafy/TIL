#include <stdio.h>

#define MAX_SIZE 100

int heap[MAX_SIZE];
int heapsize = 0;

void heapInit(void) {
	heapsize = 0;
}

void push(int data) {
	int target = heapsize + 1;
	while (target != 1 && heap[target / 2] < data) {
		heap[target] = heap[target / 2];
		target /= 2;
	}
	heap[target] = data;
	++heapsize;
}

void pop(int *value) {
	if (heapsize < 1) {
		return;
	}
	int parent = 1, child = 2;
	int temp = heap[heapsize];
	while (child < heapsize) {
		if (child + 1 < heapsize && heap[child] < heap[child + 1]) {
			++child;
		}
		if (temp >= heap[child]) {
			break;
		}
		
	}
}