#include <iostream>
using namespace std;

int T, N;
long long arr[200000][2], result;

void quickSort(int first, int last) {
	int pivot;
	int i;
	int j;
	long long tempA, tempB;


	if (first < last) {
		pivot = first;
		i = first;
		j = last;

		while (i < j) {
			while ((arr[i][0] - 1) / arr[i][1] >= (arr[pivot][0] - 1) / arr[pivot][1] && i < last) {
				i++;
			}
			while ((arr[j][0] - 1) / arr[j][1] < (arr[pivot][0] - 1) / arr[pivot][1]) {
				j--;
			}
			if (i < j) {
				tempA = arr[i][0], tempB = arr[i][1];
				arr[i][0] = arr[j][0], arr[i][1] = arr[j][1];
				arr[j][0] = tempA, arr[j][1] = tempB;
			}
		}

		tempA = arr[pivot][0], tempB = arr[pivot][1];
		arr[pivot][0] = arr[j][0], arr[pivot][1] = arr[j][1];
		arr[j][0] = tempA, arr[j][1] = tempB;

		quickSort(first, j - 1);
		quickSort(j + 1, last);
	}
}
int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		for (int n = 0; n < N; ++n) {
			scanf("%ld %ld", &arr[n][0], &arr[n][1]);
		}
		quickSort(0, N - 1);
		result = 1;
		for (int n = 0; n < N; ++n) {
			result = (arr[n][0] * result + arr[n][1]) % 1000000007;
		}
		printf("#%d %ld\n", tc, result);
	}
	return 0;
}