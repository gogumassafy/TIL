#include <iostream>
using namespace std;

#define d 259
#define m (1 << 64)

typedef struct {

} StringHash;

StringHash hs;

int T;
char input[500001], targetText[100001];

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf(" %[^\n]", &input);
		scanf(" %[^\n]", &targetText);

		printf("#%d %d\n", tc, tc);
	}
	return 0;
}