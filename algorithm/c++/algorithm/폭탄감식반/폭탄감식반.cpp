#include <iostream>
#include <string.h>
using namespace std;

int T, lengthOfString, oneOne, oneTwo, twoOne, twoTwo, flag;
char inputString[131];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%s", inputString);
		oneOne = 0;
		oneTwo = 0;
		twoOne = 0;
		twoTwo = 0;
		flag = 0;
		lengthOfString = strlen(inputString);
		for (int i = 0; i < lengthOfString - 1; ++i) {
			if (oneOne) {
				if (inputString[i] == 'C') {
					oneOne = 0;
				}
				else if (inputString[i] == 'M' && inputString[i + 1] == 'C' && inputString[i + 2] == 'M') {
					oneTwo = 1;
				}
			}

			if (twoOne) {
				if (inputString[i] == 'F') {
					twoOne = 0;
				}
				else if (inputString[i] == 'M' && inputString[i + 1] == 'F') {
					twoTwo = 1;
				}
			}

			if (!oneOne && inputString[i] == 'F' && inputString[i + 1] == 'F') {
				oneOne = 1;
			}
			if (!twoOne && inputString[i] == 'F' && inputString[i + 1] == 'C') {
				twoTwo = 1;
			}

			if ((oneOne && oneTwo) || (twoOne && twoTwo)) {
				flag = 1;
				break;
			}
		}
		if (flag) {
			printf("#%d DETECTED!\n", tc);
		}
		else {
			printf("#%d NOTHING!\n", tc);
		}
	}
	return 0;
}