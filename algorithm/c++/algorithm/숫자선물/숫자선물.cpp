#include <stdio.h>
using namespace std;

int T, nLength, flag;
char N[100001], input[2], result[100001];

int compare();
void dfs();

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%s %c %c", &N, &input[0], &input[1]);
		
	}
	return 0;
}


/*
int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%s %c %c", &N, &input[0], &input[1]);
		nLength = 0;
		for (int i = 0; i < 100001; ++i) {
			if (N[i] == '\0') {
				break;
			}
			++nLength;
		}
		for (int i = 0; i < nLength; ++i) {
			result[i] = input[0];
		}
		result[nLength] = '\0';
		if (compare() == 1) {
			flag = 0;
			if (N[0] < input[1]) {
				--nLength;
				if (nLength == 0) {
					result[0] = '-';
					result[1] = '1';
					result[2] = '\0';
				}
				else {
					for (int j = 0; j < nLength; ++j) {
						result[j] = input[1];
					}
					result[nLength] = '\0';
				}
			}
			else {
				for (int j = 0; j < nLength; ++j) {
					if (flag == 0) {
						if (N[j] >= input[1]) {
							result[j] = input[1];
							if (N[j] > input[1]) {
								flag = 1;
							}
							continue;
						}
						else if (N[j] > input[0]) {
							flag = 1;
						}
					}
					else {
						result[j] = input[1];
					}
				}
			}
		}

		else if (compare() == -1) {
			--nLength;
			if (nLength == 0) {
				result[0] = '-';
				result[1] = '1';
				result[2] = '\0';
			}
			else {
				for (int j = 0; j < nLength; ++j) {
					result[j] = input[1];
				}
				result[nLength] = '\0';
			}
		}
		if (result[0] == '0') {
			result[0] = '-';
			result[1] = '1';
			result[2] = '\0';
		}
		printf("#%d %s\n", tc, result);
	}
	return 0;
}
*/

int compare() {
	for (int i = 0; i < nLength; ++i) {
		if (N[i] < result[i]) {
			return -1;
		}
		else if (N[i] > result[i]) {
			return 1;
		}
	}
	return 0;
}

void dfs() {
	if 
	return;
}