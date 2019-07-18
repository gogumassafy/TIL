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
		flag = 1;
		lengthOfString = strlen(inputString);
		for (int i = 0; i < lengthOfString; ++i) {
			if (oneTwo) {
				if (inputString[i] == 'M') {
					continue;
				}
				if (oneTwo == 2) {
					--oneTwo;
					continue;
				}
				oneOne = 0;
				oneTwo = 0;
			}
			else if (twoTwo) {
				twoOne = 0;
				twoTwo = 0;
				continue;
			}

			if (oneOne) {
				if (inputString[i] == 'C') {
					oneOne = 0;
					flag = 0;
					break;
				}
				else if (inputString[i] == 'M' && inputString[i + 1] == 'C' && inputString[i + 2] == 'M') {
					oneTwo = 2;
				}
			}
			else if (twoOne) {
				if (inputString[i] == 'F') {
					twoOne = 0;
					flag = 0;
					break;
				}
				else if (inputString[i] == 'M' && inputString[i + 1] == 'F') {
					twoTwo = 1;
				}
			}
			else if (inputString[i] == 'F' && inputString[i + 1] == 'F') {
				oneOne = 1;
			}
			else if (inputString[i] == 'F' && inputString[i + 1] == 'C') {
				twoOne = 1;
			}
			else {
				flag = 0;
				break;
			}
		}
		if (flag && (!oneOne || oneTwo) && !twoOne) {
			printf("#%d DETECTED!\n", tc);
		}
		else {
			printf("#%d NOTHING!\n", tc);
		}
	}
	return 0;
}