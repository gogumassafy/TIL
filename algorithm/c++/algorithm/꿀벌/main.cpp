#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include  <stdio.h >

#define MAXBEE             7
#define MAXSIZE          100
#define MAXMOVECOUNT   100000 
static const double ratio = 2.0; // it will be changed

struct COORD {
    int y, x;
};

static COORD bee[MAXBEE];
static int pattern[MAXSIZE][MAXSIZE];
static int width, height, N, M;

static bool okay;
static int movecnt, moveCntLimit;
static int score;
static const int dy[5] = { 0, 0, 1, 0, -1 };
static const int dx[5] = { 0, 1, 0, -1, 0 };

extern void init(int N, COORD bee[MAXBEE]);
extern COORD make_pattern(int height, int width, int pattern[MAXSIZE][MAXSIZE]);

int moveBee(int dir[MAXBEE]) {
    if (!score)
        return score;

    movecnt++;

    if (movecnt > MAXMOVECOUNT)
        return score = 0;

    for (int i = 0; i < N; ++i) {
        if (dir[i] < 0 || dir[i] > 4) {
            return score = 0;
        }

        bee[i].y += dy[dir[i]];
        bee[i].x += dx[dir[i]];

        if (bee[i].y < 0 || bee[i].y >= MAXSIZE || bee[i].x < 0 || bee[i].x >= MAXSIZE)
            return score = 0;
    }

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j)
            if (dir[i] * dir[j] > 0 && bee[i].y == bee[j].y && bee[i].x == bee[j].x)
                return score = 0;
    }

    return 1;
}

static bool Matched(COORD start) {
    for (int i = 0; i < N; ++i) {
        int y = bee[i].y - start.y;
        int x = bee[i].x - start.x;

        if (y < 0 || y >= height || x < 0 || x >= width || pattern[y][x] == 0)
            return false;
        --pattern[y][x];
    }
    return true;
}

static void play() {
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; ++i)
        scanf("%d %d", &bee[i].y, &bee[i].x);

    init(N, bee);

    movecnt = 0;

    for (int i = 0; i < M; ++i) {

        int flower_pattern[MAXSIZE][MAXSIZE] = { { 0 } };

        scanf("%d %d %d", &height, &width, &moveCntLimit);
        for (int y = 0; y < height; ++y) {
            for (int x = 0; x < width; ++x) {
                scanf("%d", &pattern[y][x]);
                flower_pattern[y][x] = pattern[y][x];
            }
        }
        int estimate = movecnt + moveCntLimit * ratio;

        COORD patten_start = make_pattern(height, width, flower_pattern);

        if (movecnt > estimate || !Matched(patten_start))
            score = 0;
        if (score == 0) return;
    }
}

int main() {
    // freopen("input.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    int totalscore = 0;
    for (int t = 1; t <= T; ++t) {
        score = 100;
        play();
        if (score == 0) {
            totalscore = 0;
            break;
        }
        printf("#%d : %d \n", t, movecnt);
        totalscore += score;
    }
    printf("\nscore = %d\n", totalscore);
    return 0;
}