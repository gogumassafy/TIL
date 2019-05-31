#include <iostream>

int main() {
    int n, x, temp;
    scanf("%d %d", &n, &x);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &temp);
        if (temp < x) {
            printf("%d ", temp);
        }
    }
    return 0;
}