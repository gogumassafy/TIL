#define _CRT_SECURE_NO_WARNINGS 
#include<stdio.h> 

const int IDLIMIT = (int)1e5;
const int FREQUENCYLIMIT = IDLIMIT + 1;
const int RANDMULTI = 0x694F1;
const int RANDADD = 0x26A29F;
const int RANDMOD = ~(1 << 31);
const int REMOVELIMIT = 6;
const int AVGLIMIT = 4;

struct Member {
    int id, frequency;
};

extern void userInit(int memberCount, Member members[]);
extern void addMember(Member obj);
extern int removeMembers(int mode);
extern void getSum(int sum[]);

static int randSeed;
static int memberCount, orderCount;
static int idChk[IDLIMIT];
static int passCount;
static bool continuous;

static int getRandNum(void) {
    randSeed = randSeed * RANDMULTI + RANDADD;
    return randSeed & RANDMOD;
}

static int getFrequency() {
    int frequency;
    do {
        frequency = getRandNum() % FREQUENCYLIMIT;
    } while (frequency == FREQUENCYLIMIT - 1);

    return frequency;
}

static void mainInit(int tc, int n) {
    Member members[50001];

    for (int i = 0; i < n; ++i) {
        int id = getRandNum() % IDLIMIT;
        int frequency = getFrequency();
        while (idChk[id] == tc) {
            id = (id + 1) % IDLIMIT;
        }
        idChk[id] = tc;
        members[i].id = id;
        members[i].frequency = frequency;
    }
    userInit(n, members);
}

static void addFunc(int tc) {
    Member Member;
    int id = getRandNum() % IDLIMIT;
    int frequency = getFrequency();

    while (idChk[id] == tc) {
        id = (id + 1) % IDLIMIT;
    }
    idChk[id] = tc;
    Member.id = id;
    Member.frequency = frequency;
    addMember(Member);
}

static int run(int tc) {
    passCount = 0;
    bool continuous = true;

    mainInit(tc, memberCount);
    while (orderCount--) {
        int order = getRandNum() % (REMOVELIMIT + AVGLIMIT);
        if (continuous && order < AVGLIMIT) {
            int sum[2];
            int ansSum[2];
            getSum(sum);
            scanf("%d%d", &ansSum[0], &ansSum[1]);
            if (sum[0] == ansSum[0] && sum[1] == ansSum[1]) {
                ++passCount;
            }
            continuous = false;
        }
        else {
            int K = getRandNum() % 3;
            int retId, correctId;
            retId = removeMembers(K);
            scanf("%d", &correctId);
            if (retId == correctId) {
                ++passCount;
            }
            addFunc(tc);
            if (K == 1 && memberCount % 2 == 0) {
                addFunc(tc);
            }
            continuous = true;
        }
    }
    return passCount;
}

int main(void) {
    freopen("input.txt", "r", stdin);

    int TestCnt;
    int ansCount, totalScore = 0;

    scanf("%d", &TestCnt);
    setbuf(stdout, NULL);

    for (int tc = 1; tc <= TestCnt; ++tc) {
        scanf("%d%d%d%d", &randSeed, &memberCount, &orderCount, &ansCount);
        if (run(tc) == ansCount) {
            printf("#%d 100\n", tc);
            totalScore += 100;
        }
        else {
            printf("#%d 0\n", tc);
        }
    }
    printf("Total Score = %d\n", totalScore / TestCnt);
    return 0;
}