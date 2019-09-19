#include <iostream>
using namespace std;

int T, N;
long long ans, a, b, tempA, tempB, arr[200000][2];

void quickSort(int first, int last)
{
	int pivot;
	int i;
	int j;
	int temp;

	if (first < last)
	{
		pivot = first;
		i = first;
		j = last;

		while (i < j)
		{
			while ((arr[i][0] - 1) * arr[pivot][1] >= (arr[pivot][0] - 1) * arr[i][1] && i < last)
			{
				i++;
			}
			while ((arr[j][0] - 1) * arr[pivot][1] < (arr[pivot][0] - 1) * arr[j][1])
			{
				j--;
			}
			if (i < j)
			{
				tempA = arr[i][0];
				tempB = arr[i][1];
				arr[i][0] = arr[j][0];
				arr[i][1] = arr[j][1];
				arr[j][0] = tempA;
				arr[j][1] = tempB;
			}
		}

		tempA = arr[pivot][0];
		tempB = arr[pivot][1];
		arr[pivot][0] = arr[j][0];
		arr[pivot][1] = arr[j][1];
		arr[j][0] = tempA;
		arr[j][1] = tempB;

		quickSort(first, j - 1);
		quickSort(j + 1, last);
	}
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		ans = 1;
		for (int i = 0; i < N; ++i) {
			scanf("%ld %ld", &arr[i][0], &arr[i][1]);
		}
		quickSort(0, N - 1);
		for (int i = 0; i < N; ++i) {
			ans = ((long long) arr[i][0] * ans + (long long) arr[i][1]) % 1000000007;
		}
		printf("#%d %ld\n", tc, ans);
	}
	return 0;
}