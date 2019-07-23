#include <iostream>
#include <string.h>
using namespace std;

int T, K, countName, leftFlag, rightFlag, routeMap[200][200], leftIdx, rightIdx, team[200], result;
char leftMan[51], rightMan[51], nameList[200][51];


void dfs(int depth, int teamColor, int k);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		result = 1;
		countName = 0;
		scanf("%d", &K);
		memset(routeMap, 0, sizeof(routeMap));
		memset(team, 0, sizeof(team));
		for (int i = 0; i < K; ++i) {
			leftFlag = 1;
			rightFlag = 1;
			scanf("%s %s", leftMan, rightMan);
			for (int k = 0; k < countName; ++k) {
				if (strcmp(nameList[k], leftMan) == 0) {
					leftIdx = k;
					leftFlag = 0;
				}
				else if (strcmp(nameList[k], rightMan) == 0) {
					rightIdx = k;
					rightFlag = 0;
				}
				if (!leftFlag && !rightFlag) {
					break;
				}
			}
			if (leftFlag) {
				leftIdx = countName;
				strcpy(nameList[countName++], leftMan);
			}
			if (rightFlag) {
				rightIdx = countName;
				strcpy(nameList[countName++], rightMan);
			}
			routeMap[leftIdx][rightIdx] = 1;
			routeMap[rightIdx][leftIdx] = 1;
		}
		dfs(0, -1);
		if (result) {
			printf("#%d Yes\n", tc);
		}
		else {
			printf("#%d No\n", tc);
		}
	}
	return 0;
}

void dfs(int depth, int teamColor) {
	if (result == 0) {
		return;
	}
	if (depth == countName) {
		return;
	}
	if (team[depth] == 0) {
		team[depth] = teamColor;
	}
	else if (team[depth] != teamColor) {
		result = 0;
		return;
	}
	for (int i = 0; i < countName; ++i) {
		if (routeMap[depth][i] == 1) {
			if (team[i] == 0)
				team[i] = teamColor * -1;
			else if (team[i] == teamColor) {
				result = 0;
				return;
			}
		}
	}
	dfs(depth + 1, teamColor * -1);
}

void dfs(int depth, int teamColor, int k) {
	if (result == 0)
		return;
	if (depth == countName) {
		return;
	}
	for (int i = 0; i < countName; ++i) {
		if (routeMap[k][i] == 0) {
			continue;
		}
		if (team[i] == 0) {
			team[i] = teamColor * -1;
			dfs(depth + 1, teamColor * -1, i);
		}
		else if (team[i] == teamColor) {
			result = 0;
			return;
		}
	}
} 
