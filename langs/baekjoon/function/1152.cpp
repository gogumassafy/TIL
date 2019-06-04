#include <iostream>

int main() {
    int len, flag = 1, count = 0;
    char s[1000001];
    scanf("%[^\n]s", s);
    for(int i = 0; i < 1000001; ++i) {
        if(s[i] == '\0')
            break;
        if(s[i] == ' '){
            flag = 1;
            continue;
        }
        if(flag) {
            flag = 0;
            if(isalpha(s[i]))
                count++;
        }
    }
    printf("%d", count);
    return 0;
}