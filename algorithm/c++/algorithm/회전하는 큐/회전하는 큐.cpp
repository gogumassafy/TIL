#include <iostream>
using namespace std;

int N, M, A[50], total, now, moveCount[51], rightMove[51], leftMove[51], front = 1, ans = 0;

void queuePop(int number) {
	int flag = 1;
	--total;
	for (int i = number; i <= N; ++i) {
		--moveCount[i];
		if (flag && moveCount[i] != moveCount[number]) {
			flag = 0;
			now = i;
		}
	}

	if (total && flag) {
		for (int i = 1; i <= number; ++i) {
			if (moveCount[i] >= 0) {
				now = i;
				break;
			}
		}
	}
}

void selectWay(int number) {
	int rightCnt, leftCnt;
	rightCnt = moveCount[number] > moveCount[now] ? moveCount[number] - moveCount[now] : moveCount[now] - moveCount[number];
	leftCnt = total - rightCnt;

	if (rightCnt > leftCnt) ans += leftCnt;
	else ans += rightCnt;
	
	queuePop(number);
}

int main() {
	scanf("%d %d", &N, &M);
	total = N;
	now = 1;
	for (int i = 0; i < M; ++i) {
		scanf("%d", &A[i]);
	}
	for (int i = 2; i <= N; ++i) {
		moveCount[i] = moveCount[i - 1] + 1;
	}

	for (int i = 0; i < M; ++i) {
		selectWay(A[i]);
	}

	printf("%d\n", ans);

	return 0;
}