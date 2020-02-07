#include <iostream>
using namespace std;

#define MAX_N 6000
#define MAX_TABLE 900007

typedef struct _String {
	char number[8];
	int k;

	_String() {
		number[0] = '\0';
		k = 0;
	}

	_String(char _number[], int _k) {
		int idx = 0;
		while (number[idx++] = *_number++) {

		}
		k = _k;
	}
} String;

String queue[MAX_N];
int front, rear;

int tb[MAX_TABLE];

int N, K, ans = -1, idx = 0;
char input[8];


void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(String s);
int queueDeque(String* s);
void bfs();
void calculate(char number[]);
unsigned long makeHash(const char* str);

int main() {
	while (scanf("%c", &input[idx++])) {
		if (input[idx - 1] == ' ') {
			--idx;
			input[idx] = '\0';
			break;
		}
	}
	scanf("%d", &K);

	queuePush(String(input, 0));
	bfs();

	printf("%d", ans);
	return 0;
}

void calculate(char number[]) {
	int temp = 0, ten = 1;
	for (int i = idx - 1; i >= 0; --i) {
		temp += (number[i] - '0') * ten;
		ten *= 10;

		if (temp > ans) ans = temp;
	}
}

void bfs() {
	char next[8], temp;
	String s;
	unsigned long key;
	while (!queueIsEmpty()) {
		queueDeque(&s);
		if (s.k == K) {
			// 정답 갱신
			calculate(s.number);
			continue;
		}

		for (int i = 0; i <= idx; ++i) {
			next[i] = s.number[i];
		}

		for (int i = 0; i < idx; ++i) {
			for (int j = i + 1; j < idx; ++j) {
				temp = next[i];
				next[i] = next[j];
				next[j] = temp;
				// 마지막 변경 직전에는 0으로 시작하며 안됨.
				if (next[0] == '0') {
					next[j] = next[i];
					next[i] = temp;
					continue;
				}

				// 해시 테이블에 존재하면 안됨.
				key = makeHash(next);
				if (tb[key] == s.k + 1) {
					next[j] = next[i];
					next[i] = temp;
					continue;
				}

				tb[key] = s.k + 1;
				queuePush(String(next, s.k + 1));
				next[j] = next[i];
				next[i] = temp;
			}
		}
	}
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

int queuePush(String s) {
	if (queueIsFull()) return 0;

	queue[rear++] = s;
	if (rear == MAX_N) rear = 0;
	return 1;
}

int queueDeque(String* s) {
	if (queueIsEmpty()) return 0;

	*s = queue[front++];
	if (front == MAX_N) front = 0;
	return 1;
}

unsigned long makeHash(const char* str) {
	unsigned long hash = 0;
	int c;

	while (c = *str++) {
		hash = hash * 997 + c;
	}

	return hash % MAX_TABLE;
}