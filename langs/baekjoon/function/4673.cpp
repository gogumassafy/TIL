#include <iostream>

int a[10001] = {0,};

void d(int n) {
    int temp = n;
    while(n) {
        temp += n % 10;
        n /= 10;
        if (temp > 10000) {
            return;
        }
    }
    a[temp]++;
}

int main() {
    for (int i = 1; i < 10001; ++i) {
        d(i);
        if (!a[i])
            printf("%d\n", i);
    }
    return 0;
}