#include <iostream>
#include <string.h>
using namespace std;

int T, lengthOfString, oneOne, oneTwo, twoOne, twoTwo, flag;
char inputString[131];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%s", inputString);
		lengthOfString = strlen(inputString);
		flag = 1;
		for (int i = 1; i < lengthOfString; ++i) {
			if (!oneOne && !twoOne && inputString[i - 1] == 'F') {
				if (inputString[i] == 'F') {
					oneOne = 1;
				}
				else if (inputString[i] == 'C') {
					twoOne = 1;
				}
			}
			if (oneOne && !oneTwo) {
				if (inputString[i] == 'F') {
					continue;
				}
				else if (inputString[i] == 'M') {
					oneTwo = 2;
				}
				else {
					flag = 0;
					break;
				}
			}
			else if (twoOne) {

			}
			if (oneTwo) {
				if (oneTwo == 2) {
					if (inputString[i] == 'C') {
						oneTwo--;
						continue;
					}
					else {
						flag = 0;
						break;
					}
				}
				else if (oneTwo == 1) {
					if (inputString[i] == 'M') {
						continue;
					}
					else
				}
			}
		}
	}
	return 0;
}