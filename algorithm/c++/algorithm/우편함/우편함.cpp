#include <iostream>
using namespace std;

int T, N, A, B, countLetter, letter[100], time_now, head;
float rotationNum;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc < T + 1; ++tc) {
		countLetter = 0;
		head = 0;
		time_now = 0;
		scanf("%d %d %d", &N, &A, &B);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &letter[i]);
		}
		printf("#%d ", tc);
		while (head < N) {
			for (int i = 0; i < N; ++i) {
				if (time_now == letter[i])
					countLetter++;
			}
			if (B + letter[head] == time_now || countLetter == A) {
				rotationNum = countLetter / 2.0;
				for (int i = 0; i < rotationNum; ++i) {
					head++;
					countLetter--;
					printf("%d ", time_now);
				}
			}
			time_now++;
		}
		printf("\n");
	}
	return 0;
}