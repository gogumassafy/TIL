#include <iostream>
#include <cmath>

int main() {
    int n, k;
    std::string s1 = "  *   ";
    std::string s2 = " * *  ";
    std::string s3 = "***** ";
    scanf("%d", &n);
    k = log2(n / 3);
    // printf("%d", k);
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < 3*pow(2, k - i) - 1; ++j) {
            printf(" ");            
        }
        printf("*");
        for (int j = 0; j < 3*pow(2, k - i) - 1; ++j) {
            printf(" ");            
        }
        printf("*\n");
        
    }
    return 0;
}


