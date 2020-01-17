#include <iostream>
using namespace std;

int N, ans;
int A[50], B[50];

void quickSort(int input[], int first, int last);

int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &A[i]);
	}

	for (int i = 0; i < N; ++i) {
		scanf("%d", &B[i]);
	}

	quickSort(A, 0, N - 1);
	quickSort(B, 0, N - 1);

	for (int i = 0; i < N; ++i) {
		ans += B[i] * A[N - 1 - i];
	}

	printf("%d\n", ans);
	return 0;
}

void quickSort(int input[], int first, int last) {
	int pivot;
	int i;
	int j;
	int temp;

	if (first < last) {
		pivot = first;
		i = first;
		j = last;

		while (i < j) {
			while (input[i] <= input[pivot] && i < last) {
				++i;
			}
			while (input[j] > input[pivot]) {
				--j;
			}
			if (i < j) {
				temp = input[i];
				input[i] = input[j];
				input[j] = temp;
			}
		}

		temp = input[pivot];
		input[pivot] = input[j];
		input[j] = temp;

		quickSort(input, first, j - 1);
		quickSort(input, j + 1, last);
	}
}