#include <iostream>

int main() {
    int n, sumNum;
    std::cin >> n;
    sumNum = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%1d", &temp);
        sumNum += temp;
    }
    printf("%d", sumNum);
    return 0;
}