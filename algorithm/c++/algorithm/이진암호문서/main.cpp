#ifndef _CRT_SECURE_NO_WARNINGS 
#define _CRT_SECURE_NO_WARNINGS 
#endif 

#include <stdio.h> 
const int DOC_MAX_SIZE = 288;
const int RANDMOD = ~(1 << 31);
const int RANDMULTI = 0x343fd;
const int RANDADD = 0x269ec3;

extern void restorePD(int docSize, char document[][DOC_MAX_SIZE][DOC_MAX_SIZE], char repd[][DOC_MAX_SIZE]);

static int Len;
static int Half;
static char PD[DOC_MAX_SIZE][DOC_MAX_SIZE];
static char REPD[DOC_MAX_SIZE][DOC_MAX_SIZE];
static char VDSD[6][DOC_MAX_SIZE][DOC_MAX_SIZE];
static int row[6], col[6];
static unsigned int randSeed;

static int getRandNum(void) {
    randSeed = randSeed * RANDMULTI + RANDADD;
    return (randSeed & RANDMOD) >> 16;
}

inline void Swap(int& a, int& b) { int t = a; a = b; b = t; }

static void generateDocument() {
    int i, j, r, c, k = 0;
    int ratio = getRandNum() % 5 + 1;

    for (i = 0; i < Len; ++i) {
        for (j = 0; j < Len; ++j) {
            PD[i][j] = 'A' + getRandNum() % 26;
        }
    }

    for (i = 0; i < Len; i += Half) {
        for (j = 0; j < Len; j += Half) {
            row[k] = i;
            col[k++] = j;
        }
    }

    row[4] = 3 * (getRandNum() % (Half / 3 - 1) + 1);
    col[4] = 3 * (getRandNum() % (Half / 3 - 1) + 1);

    for (i = 0; i < 4; ++i) {
        j = getRandNum() % 4;
        Swap(row[i], row[j]);
        Swap(col[i], col[j]);
    }

    int t = getRandNum() % 5;
    Swap(row[t], row[4]);
    Swap(col[t], col[4]);

    for (k = 0; k < 5; k++) {
        for (i = 0; i < Half; i++) {
            for (j = 0; j < Half; j++) {
                VDSD[k][i][j] = PD[row[k] + i][col[k] + j];
            }
        }
    }

    for (i = 0; i < (Half * Half * ratio) / 100; i++) {
        r = getRandNum() % Half;
        c = getRandNum() % Half;
        VDSD[t][r][c] = 'A' + getRandNum() % 26;
    }

    restorePD(Len, VDSD, REPD);
}

static bool compareDocument() {
    int i, j;
    for (i = 0; i < Len; i++) {
        for (j = 0; j < Len; j++) {
            if (REPD[i][j] != PD[i][j]) return false;
        }
    }
    return true;
}

int main() {
    int TC, score, totalScore = 0;
    // freopen("input.txt", "r", stdin);

    setbuf(stdout, NULL);
    scanf("%d", &TC);

    for (int i = 1; i <= TC; ++i) {
        scanf("%d%d", &randSeed, &Len);

        Half = Len / 2;
        generateDocument();

        score = 100;
        if (!compareDocument()) score = 0;

        printf("#%d %d\n", i, score);
        totalScore += score;
    }
    printf("Total Score = %d\n", totalScore / TC);

    return 0;
}