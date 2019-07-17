#include <iostream>
#include <utility>
#include <vector>
using namespace std;

int T, K, flag;
char leftMan[51], rightMan[51];
vector <string> aTeam;
vector <string> bTeam;
vector <pair<string, string>> pairList;


void dfs(int depth);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		flag = 1;
		scanf("%d", &K);
		for (int i = 0; i < K; ++i) {
			scanf("%s %s", leftMan, rightMan);
			pairList.push_back(make_pair(leftMan, rightMan));
			// aTeam.push_back(leftMan);
			// bTeam.push_back(rightMan);

		}
		if (flag) {
			printf("#%d Yes\n", tc);
		}
		else {
			printf("#%d No\n", tc);
		}
		aTeam.clear();
		bTeam.clear();
	}
	return 0;
}


void dfs(int depth) {


	return;
}