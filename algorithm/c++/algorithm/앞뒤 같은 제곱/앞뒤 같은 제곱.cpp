#include <iostream>
using namespace std;

int B, temp, bitCnt, flag, c;
char nNumber[20], ans[10];

int main() {
	scanf("%d", &B);
	for (int N = 1; N < 301; ++N) {
		bitCnt = 0, flag = 1;
		temp = N * N;
		while (temp) {
			c = temp % B + 48;
			if (c > 57) c += 7;
			
			nNumber[bitCnt++] = (char) (c);
			temp /= B;
		}
		nNumber[bitCnt] = '\0';

		for (int i = 0; i < bitCnt / 2; ++i) {
			if (nNumber[i] != nNumber[bitCnt - 1 - i]) {
				flag = 0;
				break;
			}
		}

		if (flag == 0) continue;

		temp = N;
		bitCnt = 0;
		while (temp) {
			c = temp % B + 48;
			if (c > 57) c += 7;
			ans[bitCnt++] = (char) (c);
			temp /= B;
		}

		for (int i = bitCnt - 1; i >= 0; --i) {
			printf("%c", ans[i]);
		}
		printf(" %s\n", nNumber);
	}

	return 0;
}