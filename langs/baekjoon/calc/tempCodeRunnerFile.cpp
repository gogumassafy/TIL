#include <iostream>

int main() {
    int n, q, r, a, b, result;
    std::cin >> n;
    q = n / 5;
    r = n % 5;
    while (r) {
        q += r / 3;
        r %= 3;
        // a = r / 3;
        // b = r % 3;
        if (r && q > 0) {
            q -= 1;
            r += 5;
        }
        else
            break;
    }
    r ? result = -1: result = q;
    std::cout << result;
    return 0;
}