#include <iostream>

void Print(char **arr) {
    printf("%s", "arr[i] : ");
    for(int i = 0; i < 3; ++i) {
        printf("%s", arr[i]);
    }
    printf("\n");
}

int main() {
    char arr[3][10] = {"ABC", "A CB" "AB C"};
    char *arr2 = arr[0];
    printf("%s", arr2);
    // Print(arr);
    // return 0;
    // char foo[2] = {'a', 'b'};
    // char* bar = foo;
    // printf("%c", bar[1]);
    // char foo[2] = {'a', 'b'};
    // char bar[2] = foo;
    return 0;
}