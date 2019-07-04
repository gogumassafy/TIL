#include <stdio.h>
#include <string.h>

int T, N, arr[26];


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		char string[20];
		int maxNum = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			memset(arr, 0, sizeof(arr));
			char tempString[20];
			scanf(" %[^\n]s", tempString);
			for (int j = 0; j < 20; ++j) {
				if (tempString[j] == '\0') {
					break;
				}
				int tempIdx = tempString[j] - 'A';
				if (tempIdx < 0 || tempIdx > 25)
					continue;
				arr[tempIdx]++;
			}
			int tempNum = 0;
			for (int j = 0; j < 26; ++j) {
				if (arr[j])
					tempNum++;
			}
			if (tempNum > maxNum) {
				strcpy(string, tempString);
				maxNum = tempNum;
			}
			else if (tempNum == maxNum)
			{
				int tempLen = strlen(tempString), stringLen = strlen(string), minLen;
				minLen = tempLen > stringLen ? stringLen : tempLen;
				int flag = 1;
				for (int j = 0; j < minLen; ++j) {
					if (tempString[j] == string[j])
						continue;
					else if (tempString[j] > string[j]) {
						flag = 0;
						break;
					}
					else {
						break;
					}
				}
				if (flag) {
					maxNum = tempNum;
					strcpy(string, tempString);
				}
			}
		}
		printf("#%d %s\n", tc, string);
	}
	return 0;
}