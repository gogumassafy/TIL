#include <iostream>

int main() {
    std::string a;
    while(getline(std::cin, a)) {
        std::cout << a + "\n";
    }
    return 0;
}