#include <iostream>

int main() {
    int a[3];
    scanf("%d %d %d", &a[0], &a[1], &a[2]);
    printf("%d", a[0] > a[1] ? (a[1] > a[2] ? a[1] : (a[2] > a[0] ? a[0] : a[2])) : (a[0] > a[2] ? a[0] : a[1] > a[2] ? a[2] : a[1]));
    return 0;
}