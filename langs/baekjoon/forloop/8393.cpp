#include <iostream>

int main() {
    int n, sumNum;
    std::cin >> n;
    sumNum = 0;
    for (int i = 1; i <= n; ++i) {
        sumNum += i;
    }
    printf("%d", sumNum);
    return 0;
}