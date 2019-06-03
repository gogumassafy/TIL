#include <iostream>

int main() {
    int c, n, a[1000];
    scanf("%d", &c);
    for (int i = 0; i < c; ++i) {
        int temp = 0;
        float count = 0;
        scanf("%d", &n);
        for (int j = 0; j < n; ++j) {
            scanf("%d", &a[j]);
            temp += a[j];
        }
        temp /= n;
        for (int j = 0; j < n; ++j) {
            if (a[j] > temp) {
                count += 1;
            }
        }
        count = count / n * 100;
        printf("%.3f%%\n", count);
    }    
    return 0;
}