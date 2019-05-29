#include <iostream>

int main() {
    int n, sum = 0;
    char s[100];
    std::cin >> n;
    scanf("%s", s);
    for (int i = 0; i < n; ++i) {
        sum += s[i] - '0';
    }
    printf("%d", sum);
    return 0;
}