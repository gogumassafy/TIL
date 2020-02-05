#include <iostream>
using namespace std;

#define MAX -1000000000
#define MIN 1000000000

int N, A[100], math[4], maxNum = MAX, minNum = MIN;

void dfs(int depth, int temp);

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &A[i]);
	}
	
	// µ¡¼À, »¬¼À, °ö¼À, ³ª´°¼À
	for (int i = 0; i < 4; ++i) {
		scanf("%d", &math[i]);
	}

	dfs(0, A[0]);

	printf("%d\n", maxNum);
	printf("%d\n", minNum);
	return 0;
}

void dfs(int depth, int temp) {
	if (depth == N - 1) {
		if (temp > maxNum) maxNum = temp;
		if (temp < minNum) minNum = temp;
		return;
	}

	for (int i = 0; i < 4; ++i) {
		if (math[i] == 0) continue;
		--math[i];
		if (i == 0) dfs(depth + 1, temp + A[depth + 1]);
		else if (i == 1) dfs(depth + 1, temp - A[depth + 1]);
		else if (i == 2) dfs(depth + 1, temp * A[depth + 1]);
		else dfs(depth + 1, temp / A[depth + 1]);
		++math[i];
	}
}