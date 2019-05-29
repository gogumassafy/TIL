#include <iostream>

int main() {
    int t, a, b;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
    return 0;
}