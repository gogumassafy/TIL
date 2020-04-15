#include <iostream>
using namespace std;

#define MAX_NUM 202

int comp(char* a, char* b);
int strLen(char *s);
void calc(char* a, char* b);
void copy(char* str, int num[]);
void clear(int num[]);
void add();
void minusNum();
void printAnswer();

int aCnt, bCnt, aNum[MAX_NUM], bNum[MAX_NUM], ans[MAX_NUM];
char inputA[MAX_NUM], inputB[MAX_NUM];

int main() {
	while (1) {
		scanf("%s %s", inputA, inputB);
		if (inputA[0] == '0' && inputB[0] == '0') break;
		
		clear(aNum);
		clear(bNum);
		if (comp(inputA, inputB)) calc(inputA, inputB);
		else calc(inputB, inputA);
	}
	return 0;
}

int comp(char* a, char* b) {
	aCnt = 0, bCnt = 0;

	while (*a++) {
		aCnt++;
	}

	while (*b++) {
		bCnt++;
	}

	if (aCnt != bCnt) return aCnt > bCnt;

	for (int i = 0; i < aCnt; ++i) {
		if (inputA[i] != inputB[i]) return inputA[i] > inputB[i];
	}

	return 1;
}

void calc(char* a, char* b) {
	copy(a, aNum);
	copy(b, bNum);

	add();
	printAnswer();
	clear(ans);
	minusNum();
	printAnswer();
	clear(ans);
}

void copy(char* str, int num[]) {
	int length = strLen(str);
	for (int i = length - 1, j = MAX_NUM - 1; i >= 0; --i, --j) {
		num[j] = str[i] - '0';
	}
}

void clear(int num[]) {
	for (int i = 0; i < MAX_NUM; ++i) {
		num[i] = 0;
	}
}

void add() {
	for (int i = MAX_NUM - 1; i > 0; --i) {
		ans[i] += aNum[i] + bNum[i];
		if (ans[i] >= 10) {
			++ans[i - 1];
			ans[i] %= 10;
		}
	}
}

void printAnswer() {
	int i = 0;
	while (i < MAX_NUM - 1 && ans[i] == 0) i++;
	for (; i < MAX_NUM; ++i) {
		printf("%d", ans[i]);
	}
	printf("\n");
}

void minusNum() {
	for (int i = MAX_NUM - 1; i > 0; --i) {
		ans[i] += aNum[i] - bNum[i];
		if (ans[i] < 0) {
			--ans[i - 1];
			ans[i] += 10;
		}
	}
}

int strLen(char *s) {
	int length = 0;
	while (*s++) ++length;
	return length;
}