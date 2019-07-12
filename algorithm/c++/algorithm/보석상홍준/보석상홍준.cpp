#include <iostream>
using namespace std;

int T, N, X, K, temp, money, result, total, maxIDX, tB, tP;
int price[32] = { 0, }, beauty[32] = { 0, };
float maxBPP, tmpBPP;


void select(int n, int depth, int cost, int totalBeauty);
void easysort(int n);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		money = 0;
		total = 0;
		result = 987654321;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &price[i]);
		}
		for (int i = 0; i < N; ++i) {
			scanf("%d", &beauty[i]);
			total += beauty[i];
		}
		scanf("%d %d", &X, &K);
		for (int k = 0; k < K; ++k) {
			scanf("%d", &temp);
			money += price[temp - 1];
		}
		if (total >= X) {
			easysort(N);
			select(N, 0, 0, 0);
			if (result > money) {
				result -= money;
			}
			else {
				result = 0;
			}
		}
		else {
			result = -1;
		}
		printf("#%d %d\n", tc, result);
	}
	return 0;
}

void select(int n, int depth, int cost, int totalBeauty) {
	if (totalBeauty >= X) {
		if (result > cost) {
			result = cost;
		}
		return;
	}
	if (depth == n || cost >= result) {
		return;
	}
	select(n, depth + 1, cost + price[depth], totalBeauty + beauty[depth]);
	select(n, depth + 1, cost, totalBeauty);
}

void easysort(int n) {
	for (int i = 0; i < n - 1; ++i) {
		maxBPP = (float) beauty[i] / price[i];
		maxIDX = i;
		for (int j = i + 1; j < n; ++j) {
			tmpBPP = (float) beauty[j] / price[j];
			if (tmpBPP > maxBPP) {
				maxBPP = tmpBPP;
				maxIDX = j;
			}
		}
		if (maxIDX != i) {
			tB = beauty[i];
			tP = price[i];
			beauty[i] = beauty[maxIDX];
			price[i] = price[maxIDX];
			beauty[maxIDX] = tB;
			price[maxIDX] = tP;
		}
	}
}