#include <iostream>
using namespace std;

#define d 991
#define MAX_TABLE 1000007

int tb[MAX_TABLE];
unsigned long long D;
unsigned long long base;
int T, ans, inputLength, targetLength;
char input[500001], targetText[100001];

int getLength(char* str);
unsigned long hash(const char *str);
int find(const char* key);
void add(const char* key, int idx);

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		for (int i = 0; i < MAX_TABLE; ++i) {
			tb[i] = 0;
		}
		D = 1;
		scanf(" %[^\n]", &input);
		scanf(" %[^\n]", &targetText);
		inputLength = getLength(input);
		targetLength = getLength(targetText);
		for (int i = 1; i < targetLength; ++i) {
			D *= 991;
		}
		for (int i = 0; i <= inputLength - targetLength; ++i) {
			add(input + i, i);
		}
		ans = find(targetText);
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}

int getLength(char* str) {
	int length = 0;
	while (*str++) {
		++length;
	}
	return length;
}

unsigned long long makeHash(const char* str, int flag) {
	unsigned long long c;

	if (flag == 0) {
		base = 0;
		for (int i = 0; i < targetLength; ++i) {
			c = *str++;
			base = ((base * d) + c);
		}
	}
	else {
		base -= *(str - 1) * D;
		base = (base * d) + *(str + targetLength - 1);
		
	}
	return base % MAX_TABLE;
}

int find(const char* key) {
	unsigned long long h = makeHash(key, 0);
	return tb[h];
}

void add(const char* key, int idx) {
	unsigned long long h = makeHash(key, idx);
	tb[h] += 1;
}