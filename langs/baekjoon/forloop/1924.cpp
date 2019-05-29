#include <iostream>

int main() {
    int m, d;
    std::cin >> m >> d;
    std::string days[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    int daysOfMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    for (int i = 0; i < m; ++i) {
        d +=  daysOfMonth[i];
    }
    std::cout << days[d % 7];
    return 0;
}