#include <stdio.h>
using namespace std;

int T;
int N;
int arr[100000];
int stack[100001] = { 1, 2, 3, };


int main() {
	for (int i = 1; i < 100001; ++i) {
		stack[i] = i;
	}
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		printf("#%d ", tc);

	}
	return 0;
}