#include <iostream>
using namespace std;

#define MAX_N 41

typedef struct _Count {
	int zeroCnt;
	int oneCnt;
	
	_Count() {
		zeroCnt = -1;
		oneCnt = -1;
	}
	
} Count;

Count number[MAX_N];

int T, N, zeroCnt, oneCnt;

int fibonacci(int n) {
	if (n == 0) { 
		++zeroCnt;
		return 0;
	}
	else if (n == 1) {
		++oneCnt;
		return 1;
	}
	else return fibonacci(n - 1) + fibonacci(n - 2);
}

void dp() {
	
	for (int i = 0; i <= 40; ++i) {
		if (number[i].zeroCnt == -1) {

		}
		else {

		}
	}
}

int main() {
	scanf("%d", &T);
	dp();
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		zeroCnt = 0, oneCnt = 0;

		printf("%d %d", zeroCnt, oneCnt);
	}
	return 0;
}

void dp() {

}