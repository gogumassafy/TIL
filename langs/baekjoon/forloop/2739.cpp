#include <iostream>

int main() {
    int n;
    std::cin >> n;
    for (int i = 1; i < 10; ++i) {
        printf("%d * %d = %d\n", n, i, n*i);
    }
    return 0;
}