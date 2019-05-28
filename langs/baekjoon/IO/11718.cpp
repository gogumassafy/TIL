#include <iostream>

int main () {
    std::string inputStr;
    while (1) {
        getline(std::cin, inputStr);
        if (inputStr == "")
            break;
        std::cout << inputStr << std::endl;
    }
    return 0;
}