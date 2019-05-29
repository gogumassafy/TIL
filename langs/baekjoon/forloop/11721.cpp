#include <iostream>

int main() {
    char s[10];
    while(scanf("%10s", s) == EOF) {
        printf("%s\n", s);
    }
    return 0;
}