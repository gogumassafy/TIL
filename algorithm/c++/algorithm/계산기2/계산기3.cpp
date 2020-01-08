#include <iostream>
using namespace std;

int N;
int inputIdx, postIdx, stackPoint, numIdx, numStack[200];
char input[20000], post[20000], inputStack[200];

int main() {
	for (int tc = 1; tc <= 10; ++tc) {
		scanf("%d", &N);
		inputIdx = 0, postIdx = 0, stackPoint = 0;
		scanf(" %[^\n]", input);
		while (input[inputIdx] != '\0') {
			if (input[inputIdx] >= '0' && input[inputIdx] <= '9') {
				post[postIdx++] = input[inputIdx];
			}
			else if (input[inputIdx] == '+') {
				if (stackPoint == 0 || inputStack[stackPoint - 1] == '(') inputStack[stackPoint++] = '+';
				else {
					post[postIdx++] = inputStack[stackPoint - 1];
					inputStack[stackPoint - 1] = '+';
				}

			}
			else if (input[inputIdx] == '*') {
				if (stackPoint == 0 || inputStack[stackPoint - 1] == '+' || inputStack[stackPoint - 1] == '(') inputStack[stackPoint++] = '*';
				else post[postIdx++] = '*';
			}
			else if (input[inputIdx] == ')') {
				while (inputStack[--stackPoint] != '(') {
					post[postIdx++] = inputStack[stackPoint];
					// --stackPoint;
				}
			}
			else {
				inputStack[stackPoint++] = '(';
			}
			++inputIdx;
		}

		while (stackPoint > 0) {
			post[postIdx++] = inputStack[--stackPoint];
		}
		post[postIdx] = '\0';

		numIdx = 0;
		for (int i = 0; i < postIdx; ++i) {
			if (post[i] >= '0' && post[i] <= '9') numStack[numIdx++] = post[i] - '0';
			else {
				if (post[i] == '+') {
					numStack[numIdx - 2] += numStack[numIdx - 1];

				}
				else {
					numStack[numIdx - 2] *= numStack[numIdx - 1];
				}
				--numIdx;
			}
		}
		printf("#%d %d\n", tc, numStack[0]);
	}
	return 0;
}