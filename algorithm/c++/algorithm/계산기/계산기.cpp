#include <iostream>
using namespace std;

int T, ans, inputIdx, postIdx, numStack[200000], numPoint, inputPoint;
// 입력을 받음, 후위표기식, 후위표기식을 만들기 위한 스택
char input[20000], result[200000], inputStack[200000];

int main() {
	scanf("%d\n", &T);
	for (int tc = 1; tc <= T; ++tc) {
		ans = 0, inputIdx = 0, postIdx = 0;
		scanf(" %[^\n]", input);
		while (input[inputIdx] != '\n') {
			if (input[inputIdx] == '(') {
				inputStack[inputPoint++] = '(';
			}
			else if (input[inputIdx] == ')') {
				while (inputStack[--inputPoint] != '(') {
					result[postIdx++] = inputStack[inputPoint];
				}
			}
			else if (input[inputIdx] == '+') {
				if (inputPoint == 0 || inputStack[inputPoint - 1] == '(') {
					inputStack[inputPoint++] = '+';
				}
				else {
					result[postIdx++] = inputStack[inputPoint - 1];
					inputStack[inputPoint - 1] = '+';
				}
			}
			else {
				
			}


			++inputIdx;
		}

		while (result[postIdx] != '\n') {
			if (result[postIdx] >= '0' && result[postIdx] <= '9') {
				numStack[numPoint++] = result[postIdx] - '0';
			}
			else if (result[postIdx] == '+') {
				numStack[]
			}
			else {

			}
			++postIdx;
		}
		printf("#%d %d\n", tc, ans);
	}
	return 0;
}