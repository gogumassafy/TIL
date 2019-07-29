#include <iostream>
#include <string.h>
using namespace std;

int T, N, countName, compareResult, indexOrder[20000];
char tempName[51], nameList[20000][51];

int main() {
	scanf("%d", &T);
	for (int tc = 0; tc < T + 1; ++tc) {
		countName = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%s", tempName);
			for (int j = 0; j < countName; ++j) {
				compareResult = strcmp(nameList[i], tempName);
				if (compareResult == 0) {
					break;
				}
				else if (compareResult < 0) {
					continue;
				}
				else if (compareResult > 0) {

				}
			}
		}
	}
	return 0;
}