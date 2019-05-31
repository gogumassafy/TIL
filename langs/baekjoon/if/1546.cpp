#include <iostream>

int main() {
    int n, maxScore = 0;
    scanf("%d", &n);
    float score[n], avg = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%f", &score[i]);
        if (score[i] > maxScore)
            maxScore = (int) score[i];
    }
    for (int i = 0; i < n; ++i) {
        score[i] = score[i] / maxScore * 100;
        avg += score[i];
    }
    avg /= n;
    printf("%.2f", avg);
    return 0;
}