#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#define ADDPLAYER       (1)
#define REMOVEPLAYER    (2)
#define GETRANK         (3)
#define COUNTPLAYERS    (4)

#define MAX_NAME_LEN    (12)
#define EVENT_COUNT     (5)


extern void init();
extern void addPlayer(char name[], int rscore[]);
extern void removePlayer(char name[]);
extern int  getRank(char name[], int index);
extern int  countPlayers(int lowScore, int highScore, int index);
/////////////////////////////////////////////////////////////////////////

static int run(int Ans)
{
    int N;
    int inputCnt = scanf("%d", &N);
    if (inputCnt != 1) {
        return 0;
    }

    init();

    for (int i = 0; i < N; ++i)
    {
        int cmd;
        scanf("%d", &cmd);

        char s1[MAX_NAME_LEN + 1];
        int  score[EVENT_COUNT];
        int  x1, x2, x3, ret, ans;

        switch (cmd)
        {
        case ADDPLAYER:
            scanf("%s", s1);
            for (int i = 0; i < EVENT_COUNT; ++i)
            {
                scanf("%d", &score[i]);
            }

            addPlayer(s1, score);
            break;

        case REMOVEPLAYER:
            scanf("%s", s1);

            removePlayer(s1);
            break;

        case GETRANK:
            scanf("%s %d", s1, &x1);

            ret = getRank(s1, x1);

            scanf("%d", &ans);
            if (ret != ans)
            {
                Ans = 0;
            }
            break;

        case COUNTPLAYERS:
            scanf("%d %d %d", &x1, &x2, &x3);

            ret = countPlayers(x1, x2, x3);

            scanf("%d", &ans);
            if (ret != ans)
            {
                Ans = 0;
            }
            break;
        }
    }

    return Ans;
}

int main()
{
    setbuf(stdout, NULL);
    freopen("input.txt", "r", stdin);

    int T, Ans;
    scanf("%d %d", &T, &Ans);

    for (int tc = 1; tc <= T; tc++)
    {
        printf("#%d %d\n", tc, run(Ans));
    }

    return 0;
}