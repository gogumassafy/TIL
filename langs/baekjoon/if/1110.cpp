#include <iostream>

int main() {
    int n, a, b, temp, count = 0;

    scanf("%d", &n);
    temp = n;
    do {
        a = temp % 10;
        b = temp / 10;
        temp = a + b;
        temp = temp % 10 + a * 10;
        ++count;
    } 
    while (n != temp);
    printf("%d", count);
    return 0;
}