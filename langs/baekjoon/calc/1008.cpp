#include <iostream>

int main() {
    double a, b;
    std::cin >> a >> b;
    std::cout.precision(15);
    std::cout << a / b;
    return 0;    
}