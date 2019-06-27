#include <stdio.h>
#include <algorithm>
using namespace std;
int T, P, maxNum, result, flag, q, r;

int main() {
    
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d", &P);
        int arr[P];
        for (int i = 0; i < P; ++i) {
            scanf("%d", &arr[i]);
        }
        maxNum = *max_element(arr, arr + P);
        for (int i = 0; i < P; ++i) {
            result = maxNum * arr[i];
            flag = 1;
            for (int j = 0; j < P; ++j) {
                q = result / arr[j];
                r = result % arr[j];
                if (none_of(arr, arr + P, [](int x){ return x == q; }) || r) {
                    flag = 0;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }
        printf("#%d %d\n", tc, result);
    }
    return 0;
}