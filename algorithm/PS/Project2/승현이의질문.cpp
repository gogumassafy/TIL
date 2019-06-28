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
		vector<int> countNum(1000001);
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &temp);
			if (countNum[temp] == 0)
				v.push_back(temp);
			countNum[temp] += 1;
		}
		v.push_back(0);
		sort(v.begin(), v.end());
		for (int i = v.size() - 1; i > 0; --i) {
			countNum[v[i - 1]] += countNum[v[i]];
		}
		for (int i = v.size() - 1; i > 0; --i) {
			if (v[i - 1] <= countNum[v[i]]) {
				result = countNum[v[i]] > v[i] ? v[i] : countNum[v[i]];
				break;
			}
		}
		printf("#%d %d\n", tc, result);
		v.clear();
	}
	return 0;
}