#include <iostream>
#include <cstring>

int main() {
    int t, n, idx, maxIdx = 0, alphabet[26];
    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        scanf("%d", &n);
        char name[n][21];
        int total[n];
        memset(total, 0, sizeof(total));
        for (int i = 0; i < n; ++i) {
            memset(alphabet, 0, sizeof(alphabet));
            scanf(" %[^\n]s", name[i]);
            for (int j = 0; j < 21; ++j) {
                if (name[i][j] == '\0') {
                    break;
                }
                idx = (int) name[i][j] - (int) 'A';
                if (idx >= 0 && alphabet[idx] == 0) {
                    total[i]++;
                    alphabet[idx] = 1;
                }
            }
        }

        for (int i = 1; i < n; ++i) {
            if(total[i] > total[maxIdx]) {
                maxIdx = i;
            }
            else if(total[i] == total[maxIdx]) {
                for (int j = 0; j < 21; ++j) {
                    if (name[i][j] == '\0') {
                        maxIdx = i;
                        break;
                    }
                    else if (name[maxIdx][j] == '\0') {
                        break;
                    }

                    if ((int) name[i][j] < (int) name[maxIdx][j]) {
                        maxIdx = i;
                        break;
                    }
                    else if ((int) name[i][j] > (int) name[maxIdx][j]) {
                        break;
                    }
                }
            }
        }
        printf("#%d %s %d\n", tc, name[maxIdx], total[maxIdx]);
    }
    return 0;
}



// 2
// 5
// BBIBBI
// DEAD BEEF
// ABCDDCBA
// ABCDDCBA
// ABCDEFGHIJKL
// 2
// ABC
// AAAA BBBB CCCC