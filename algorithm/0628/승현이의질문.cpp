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
		for (int i = v.size() - 1; i > 0; --i) {
            temp = pv[sieze - 1].first;
            if (temp != v[i]) {
                pv.push_back(make_pair(v[i], 1));
            }
            else {
                ++pv[size - 1].second;
            }
		}
		for (int i = pv.size() - 1; i > 0; --i) {
			if (pv[i - 1].first <= pv[i].second) {
				result = pv[i].second > pv[i - 1].first ? pv[i - 1].first: pv[i].second;
				break;
			}
		}
		printf("#%d %d\n", tc, result);
		v.clear();
        pv.clear();
	}
	return 0;
}
