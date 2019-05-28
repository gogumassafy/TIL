#include<cstdio>
char a[102];
int main() {
	while (scanf("%[^\n]\n", a) == 1) {
		printf("%s\n", a);
	}
}