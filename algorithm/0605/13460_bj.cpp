#include <iostream>

int main() {
    int N, M;
    char arr[N][M];
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; ++i) {
        scanf("%s", arr[i]);
    }
    return 0;
}