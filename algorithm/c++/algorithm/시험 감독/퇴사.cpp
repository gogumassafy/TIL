#include <iostream>
using namespace std;

#define MAX_N 15

typedef struct _Schedule {
	int t;
	int p;

} Schedule;

Schedule schedule[MAX_N];

int N, ans = 0;

void dfs(int k, int sum);

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		int t, p;
		scanf("%d %d", &t, &p);
		schedule[i].t = t;
		schedule[i].p = p;
	}
	dfs(0, 0);
	printf("%d\n", ans);
	return 0;
}

void dfs(int k, int sum) {
	if (sum > ans) ans = sum;

	for (int i = k; i < N; ++i) {
		if (i + schedule[i].t > N) continue;
		dfs(i + schedule[i].t, sum + schedule[i].p);
	}
}