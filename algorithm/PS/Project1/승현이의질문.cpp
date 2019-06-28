#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int T;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		int N, temp, result = 0;
		vector<int> v;
		vector<pair<int, int>> pv;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &temp);
			v.push_back(temp);
		}
		sort(v.begin(), v.end());
		pv.push_back(make_pair(v[v.size() - 1], 1));
		for (int i = v.size() - 2; i >= 0; --i) {
			temp = pv[pv.size() - 1].first;
			if (temp != v[i]) {
				temp = pv[pv.size() - 1].second;
				pv.push_back(make_pair(v[i], temp + 1));
			}
			else {
				++pv[pv.size() - 1].second;
			}
		}
		pv.push_back(make_pair(0, pv[pv.size() - 1].second));
		for (int i = 0; i < pv.size() - 1; ++i) {
			if (pv[i + 1].first <= pv[i].second) {
				result = pv[i].second > pv[i].first ? pv[i].first : pv[i].second;
				break;
			}
		}
		printf("#%d %d\n", tc, result);
		v.clear();
		pv.clear();
	}
	return 0;
}
