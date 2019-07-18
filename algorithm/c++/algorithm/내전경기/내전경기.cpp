#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int T, K, flag;
char leftMan[51], rightMan[51];
vector <string> team;
vector <pair<string, string>> pairList;
vector <string>::iterator it;


void dfs(int depth);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		flag = 1;
		scanf("%d", &K);
		for (int i = 0; i < K; ++i) {
			scanf("%s %s", leftMan, rightMan);
			it = find(team.begin(), team.end(), leftMan);
			if (it) {

			}
			// pairList.push_back(make_pair(leftMan, rightMan));


		}
		if (flag) {
			printf("#%d Yes\n", tc);
		}
		else {
			printf("#%d No\n", tc);
		}
		// aTeam.clear();
		// bTeam.clear();
	}
	return 0;
}


void dfs(int depth) {


	return;
}