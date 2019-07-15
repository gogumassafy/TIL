#include <iostream>
#include <string.h>
using namespace std;

int T, result, lengthOfString, countPal, leftNum, rightNum, flag;
char str[1001];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%s", str);
		result = 0;
		lengthOfString = strlen(str);
		for (int i = 0; i < lengthOfString; ++i) {
			for (int j = lengthOfString - 1; j >= 0; --j) {
				flag = 1;
				leftNum = i;
				rightNum = j;
				while (leftNum <= rightNum) {
					if (str[leftNum] != str[rightNum]) {
						flag = 0;
						break;
					}
					++leftNum;
					--rightNum;
				}
				if (flag)
					countPal = j - i + 1;
					result = countPal > result ? countPal : result;
			}
		}
		printf("#%d %d\n", tc, result);
	}
	return 0;
}