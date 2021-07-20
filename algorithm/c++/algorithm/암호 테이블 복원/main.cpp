#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

const int MAXN = 64;
const int ALPHA = 26;
static int tableSize;
static int maxQueryLimit;
static int MOD = 31;
static int tcScore, queryCount, emptyCount;
static char pollute[MAXN + 1][MAXN + 1];
static char charTable[MAXN + 1][MAXN + 1];

extern void repair(int, int, char[][MAXN + 1]);

static void initialize()
{
    tcScore = queryCount = emptyCount = 0;
    memset(pollute, 0, sizeof(pollute));
    memset(charTable, 0, sizeof(charTable));
}

void query(char sector[][4])
{
    queryCount++;
    int i, j;
    int r = rand() % MOD * 2, c = rand() % MOD * 2;
    for (i = 0; i < 4; ++i)for (j = 0; j < 4; ++j)
    {
        sector[i][j] = charTable[i + r][j + c];
    }
}

static void input()
{
    scanf("%d %d", &tableSize, &maxQueryLimit);
    MOD = (tableSize - 4) / 2 + 1;
    for (int i = 0; i < tableSize; ++i)
        scanf("%s", charTable[i]);
    for (int i = 0; i < tableSize; ++i)
    {
        for (int j = 0; j < tableSize; ++j)
        {
            if (i < 2 || j < 2 || i >= tableSize - 2 || j >= tableSize - 2)
                pollute[i][j] = charTable[i][j];
            else
            {
                pollute[i][j] = '*';
                emptyCount++;
            }
        }
    }
}

static void makeData()
{
    tableSize = 64;
    maxQueryLimit = 4096;
    MOD = (tableSize - 4) / 2 + 1;
    int i, j;
    for (i = 0; i < tableSize; ++i)
    {
        for (j = 0; j < tableSize; ++j)
        {
            charTable[i][j] = rand() % 15 + 'A';
            if (i < 2 || j < 2 || i >= tableSize - 2 || j >= tableSize - 2)
                pollute[i][j] = charTable[i][j];
            else
            {
                pollute[i][j] = '*';
                emptyCount++;
            }
        }
    }
}

static void process()
{
    repair(tableSize, maxQueryLimit, pollute);
    if (queryCount > maxQueryLimit) return;
    int i, j, correctCnt = 0;
    for (i = 0; i < tableSize; ++i)
    {
        for (j = 0; j < tableSize; ++j)
        {
            if (charTable[i][j] == pollute[i][j])
                correctCnt++;
        }
    }
    if (correctCnt >= tableSize * tableSize * 95 / 100)
    {
        tcScore = 100;
    }
}

int main()
{
    srand(2);
    int testCase = 50;
    scanf("%d", &testCase);
    for (int tc = 1; tc <= testCase; ++tc)
    {
        initialize();
        input();
        //makeData();
        process();
        printf("# %d : %d\n", tc, tcScore);
    }
    return 0;
}