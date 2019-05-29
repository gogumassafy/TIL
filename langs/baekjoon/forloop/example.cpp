#include <iostream>
#include <cstring>

int main() {
    char s[11];
    int i = 123;
    float f = 1233.34;
    // strcpy(s, "hello");
    scanf("%[^abc]", s);

    printf("%10s\n", s);
    printf("%-10s\n", s);
    printf("%10.2s\n", s);

    printf("%010d\n", i);
    printf("% 10d\n", i);
    printf("% 1d\n", i);
    printf("% d\n", i);
    printf("%d\n", i);
    printf("%.1d\n", i);

    printf("%f\n", f);
    printf("%10f\n", f);
    printf("%f\n", f);
    printf("%.1f\n", f);
}