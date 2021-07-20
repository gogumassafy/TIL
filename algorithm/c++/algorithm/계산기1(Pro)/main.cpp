#include <stdio.h>
#include <string.h>
#define MAX 50
#define LIMIT 100000
#define WORNG_ANSWER -1

static char problem[MAX * 20 + 5];
static char ret[LIMIT + MAX * 20];
static char str[MAX + 5];
char user[MAX + 5];

extern void Cal(char ch, char* user);

int main(void) {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int TC, t;
    scanf("%d", &TC);
    fgets(str, MAX + 5, stdin);

    for (t = 1; t <= TC; ++t) {
        fgets(problem, MAX * 20 + 5, stdin);
        int pLen = strlen(problem);
        while (problem[pLen - 1] == '\n' || problem[pLen - 1] == '\r')
            problem[--pLen] = '\0';
        memset(ret, 0, sizeof(ret));
        int uLen = 0, retIdx = 0;

        Cal('C', user);
        user[MAX + 1] = 0;
        uLen = strlen(user);
        sprintf(ret + retIdx, "%s ", user);
        retIdx += uLen + 1;

        for (int i = 0; i < pLen;) {
            sscanf(problem + i, "%s", str);
            int slen = strlen(str);
            i += slen + 1;
            if (str[0] >= '0' && str[0] <= '9') {
                for (int j = 0; j < slen; ++j) {
                    Cal(str[j], user);
                    user[MAX + 1] = 0;
                    uLen = strlen(user);
                    sprintf(ret + retIdx, "%s ", user);
                    retIdx += uLen + 1;
                }
            }
            else {
                Cal(str[0], user);
                user[MAX + 1] = 0;
                uLen = strlen(user);
                sprintf(ret + retIdx, "%s ", user);
                retIdx += uLen + 1;
            }
        }
        puts(ret);
    }
    return 0;
}