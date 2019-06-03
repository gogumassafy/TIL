#include <iostream>

int main() {
    int n, a, b, d, temp, flag = 1, count = 0;
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
        if (i < 100) {
            count++;
            continue;
        }
        temp = i;
        flag = 1;
        a = temp % 10;
        temp /= 10;
        b = temp % 10;
        temp /= 10;
        d = b - a;
        while (temp) {
            a = b;
            b = temp % 10;
            temp /= 10;
            if (b != a + d) {
                flag = 0;
                break;
            }
        }
        if (flag == 1)
            count++;
    }
    printf("%d", count);
    return 0;
}