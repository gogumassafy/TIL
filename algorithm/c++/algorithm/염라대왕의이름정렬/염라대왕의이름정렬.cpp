#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

int T, N, countName, compareResult, flag, bookIndex;
char tempName[51];
vector <string> nameList;

bool cmp(string left, string right);

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%s", tempName);
			nameList.push_back(tempName);
		}
		sort(nameList.begin(), nameList.end(), cmp);
		nameList.erase(unique(nameList.begin(), nameList.end()), nameList.end());
		printf("#%d\n", tc);
		for (size_t i = 0; i < nameList.size(); ++i) {
			printf("%s\n", nameList[i].c_str());
		}
		nameList.clear();
	}
	return 0;
}

bool cmp(string left, string right) {
	if (left.size() < right.size()) {
		return true;
	}
	else if (left.size() == right.size()) {
		return left < right;
	}
	return false;
}