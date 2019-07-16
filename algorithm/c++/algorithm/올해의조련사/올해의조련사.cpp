#include <iostream>
using namespace std;

int T, N;
char inputLine[2001], temp, result[2001];


void makeNew(int depth, int start, int end);


int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%c", &temp);
			inputLine[i] = temp;
		}
		makeNew(0, 0, N - 1);
	}
	return 0;
}


void makeNew(int depth, int start, int end) {
	if (depth == N) {
		return;
	}

}