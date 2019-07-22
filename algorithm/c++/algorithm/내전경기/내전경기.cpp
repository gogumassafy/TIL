#include <iostream>
#include <string.h>
using namespace std;

int T, K, countName, leftFlag, rightFlag, routeMap[200][200];
char leftMan[51], rightMan[51], nameList[200][51];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		countName = 0;
		scanf("%d", &K);
		memset(routeMap, 0, sizeof(routeMap));
		for (int i = 0; i < K; ++i) {
			leftFlag = 1;
			rightFlag = 1;
			scanf("%s %s", leftMan, rightMan);
			for (int k = 0; k < countName; ++k) {
				if (strcmp(nameList[k], leftMan)) {
					leftFlag = 0;
				}
				else if (strcmp(nameList[k], rightMan)) {
					rightFlag = 0;
				}
				if (!leftFlag && !rightFlag) {
					break;
				}
			}
			if (leftFlag) {

				strcpy(nameList[countName++], leftMan);
			}
			if (rightFlag) {
				strcpy(nameList[countName++], rightMan);
			}
		}
	}
	return 0;
}