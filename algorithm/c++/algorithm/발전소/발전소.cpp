#include <iostream>
using namespace std;

int N, cost[16][16], isOn[16], P;

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			scanf("%d", &cost[i][j]);
		}
	}

	char temp;
	for (int i = 0; i < N; ++i) {
		scanf(" %c", &temp);
		if (temp == 'Y') isOn[i] = 1;
	}

	scanf("%d", &P);
	return 0;
}