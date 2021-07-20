/// *** main.cpp ***
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#define MAXN 1000000

using namespace std;

static int orgArr[MAXN], removeArr[MAXN], answer[1000], userAns[1000];
static int nCount, userCount;
int orgCount, removeCount, answerCount;
static void SWAP(int& x, int& y) { int z = x; x = y; y = z; }

extern int card_find(int userAns[]);

int getRand() {
    return rand() % 1000;
}

int getNumber(int dir, int num) {
    nCount++;
    if (num < 0 || num >= MAXN) return 0;
    if (dir == 1) return orgArr[num];
    else if (dir == 2) return removeArr[num];
    else return 0;
}

void input() {
    scanf("%d %d", &orgCount, &removeCount);
    int i;
    for (i = 0; i < orgCount; ++i) scanf("%d", orgArr + i);
    for (i = 0; i < removeCount; ++i) scanf("%d", removeArr + i);
    answerCount = orgCount - removeCount;
    for (i = 0; i < answerCount; ++i) scanf("%d", answer + i);
}

void init(int t) {
    int i, j, k, delno;
    nCount = 0;
    orgCount = (getRand() * 100 + getRand()) % 100000 + 100000 * (t + 1);
    answerCount = rand() % 100 + 100 * (t + 1);
    if (orgCount > MAXN) orgCount = MAXN;
    if (answerCount > 1000) answerCount = 1000;
    removeCount = orgCount - answerCount;

    for (i = 0; i < MAXN; i++) orgArr[i] = removeArr[i] = 0;
    for (i = 0; i < 1000; i++) userAns[i] = answer[i] = 0;
    for (i = 0; i < orgCount; i++) orgArr[i] = i + 1;
    for (i = 0; i < orgCount; i++) {
        SWAP(orgArr[i], orgArr[(getRand() * 100 + getRand()) % orgCount]);
    }
    for (i = 0; i < orgCount; i++) removeArr[i] = orgArr[i];

    for (i = 0; i < answerCount; i++) {
        do {
            delno = (getRand() * 100 + rand()) % orgCount;
        } while (removeArr[delno] == 0);
        removeArr[delno] = 0;
    }
    for (i = j = k = 0; i < orgCount; i++) {
        if (removeArr[i]) {
            removeArr[i] = 0;
            removeArr[j++] = orgArr[i];
        }
        else answer[k++] = orgArr[i];
    }
}

int check() {
    if (answerCount != userCount)
        return MAXN;
    for (int i = 0; i < answerCount; i++) {
        if (answer[i] != userAns[i])
            return MAXN;
    }
    return nCount;
}

int main(void) {

    int testCase;

#if 0  /// 1:file_IO or 0:ramdom generate

    //freopen("input.txt", "r", stdin);
    scanf("%d", &testCase);
    for (int tc = 1; tc <= testCase; tc++) {
        input();
        userCount = card_find(userAns);
        nCount = check();
        printf("#%d : %d\n", tc, nCount);
        if (nCount == MAXN) break;
    }

#else

    testCase = 50;
    srand(2018);
    for (int tc = 1; tc <= testCase; tc++) {
        init(tc);
        userCount = card_find(userAns);
        nCount = check();
        printf("#%d : %d\n", tc, nCount);
        if (nCount == MAXN) break;
    }

#endif

    return 0;
}