/// === sol.cpp ===
#ifndef NULL
#define NULL  0
#endif

struct Member {
    int id, frequency;
};

/// === submit area start ===
#define MAXN 50000
#define MAXID 100000
#define MAXF 100001
#define MINF -1

int lastNode[4], memberPos[MAXID + 1][4], inf[2] = { MAXF, MINF };
// 0은 max, 1은 min, 2는 max, 3은 min

Member heap[4][MAXN + 1];

int check(int idx, Member* a, Member* b) {
    // min
    if (idx % 2) {
        if (a->frequency > b->frequency) return 0;
        if (a->frequency == b->frequency && a->id > b->id) return 0;
    }
    // max
    else {
        if (a->frequency < b->frequency) return 0;
        if (a->frequency == b->frequency && a->id < b->id) return 0;
    }
    return 1;
}

void upward(int idx, int start) {
    int p, c;

    c = start, p = c / 2;

    while (p) {
        if (check(idx, &heap[idx][p], &heap[idx][c])) break;

        Member tmp;
        tmp = heap[idx][p];
        heap[idx][p] = heap[idx][c];
        memberPos[heap[idx][p].id][idx] = p;
        heap[idx][c] = tmp;
        memberPos[heap[idx][c].id][idx] = c;

        c = p, p = c / 2;
    }
}

void downward(int idx, int start) {
    int p, c, l, r;

    p = start, l = 2 * p, r = l + 1;

    while (l <= lastNode[idx]) {
        if (l == lastNode[idx] || check(idx, &heap[idx][l], &heap[idx][r])) c = l;
        else c = r;

        if (check(idx, &heap[idx][p], &heap[idx][c])) break;

        Member tmp;
        tmp = heap[idx][p];
        heap[idx][p] = heap[idx][c];
        memberPos[heap[idx][p].id][idx] = p;
        heap[idx][c] = tmp;
        memberPos[heap[idx][c].id][idx] = c;

        p = c, l = p * 2, r = l + 1;
    }
}

void heapPush(int idx, Member* a) {
    int c;

    heap[idx][++lastNode[idx]] = *a;
    c = lastNode[idx];
    memberPos[heap[idx][c].id][idx] = c;

    upward(idx, c);
}

Member heapPop(int idx) {
    Member res;

    res = heap[idx][1];
    memberPos[heap[idx][1].id][idx] = 0;
    heap[idx][1] = heap[idx][lastNode[idx]--];
    memberPos[heap[idx][1].id][idx] = 1;

    downward(idx, 1);

    return res;
}

void addMember(Member obj) {
    Member res;

    for (int idx = 1; idx < 4; ++idx) {
        heapPush(idx, &obj);
    }

    if (lastNode[1] > lastNode[0] + 1) {
        res = heapPop(1);
        heapPush(0, &res);
    }
    else if (heap[0][1].frequency >= heap[1][1].frequency) {
        res = heapPop(1);
        heapPush(0, &res);
        res = heapPop(0);
        heapPush(1, &res);
    }
}

int removeMembers(int mode) {
    int res = 0;
    Member tmp;

    if (mode == 0) {
        tmp = heapPop(3);
    }
    else if (mode == 1) {
        if (lastNode[0] == lastNode[1]) {
            tmp = heapPop(0);
            res += tmp.id;

            for (int i = 0; i < 4; ++i) {
                int x = memberPos[tmp.id][i];
                if (x == 0) continue;
                heap[i][x].frequency = inf[i % 2];
                upward(i, x);
                heapPop(i);
            }
        }

        tmp = heapPop(1);
    }
    else {
        tmp = heapPop(2);
    }

    for (int i = 0; i < 4; ++i) {
        int x = memberPos[tmp.id][i];
        if (x == 0) continue;
        heap[i][x].frequency = inf[i % 2];
        upward(i, x);
        heapPop(i);
    }

    if (lastNode[1] > lastNode[0] + 1) {
        Member res = heapPop(1);
        heapPush(0, &res);
    }
    else if (lastNode[1] < lastNode[0]) {
        Member res = heapPop(0);
        heapPush(1, &res);
    }

    res += tmp.id;

    return res;
}

void getSum(int sum[]) {
    sum[0] = 0, sum[1] = 0;
    for (int i = 1; i <= lastNode[0]; ++i) {
        sum[0] += heap[0][i].frequency;
        sum[1] += heap[1][i].frequency;
    }

    if (lastNode[1] > lastNode[0]) {
        sum[1] += heap[1][lastNode[1]].frequency - heap[1][1].frequency;
    }
}

void userInit(int memberCount, Member members[]) {
    lastNode[0] = lastNode[1] = lastNode[2] = lastNode[3] = 0;

    for (int i = 0; i < MAXID + 1; ++i) {
        memberPos[i][0] = memberPos[i][1] = memberPos[i][2] = memberPos[i][3] = 0;
    }

    for (int i = 0; i < memberCount; ++i) {
        for (int idx = 1; idx < 4; ++idx) {
            heapPush(idx, members + i);
        }
    }

    while (lastNode[1] > lastNode[0] + 1) {
        Member res = heapPop(1);
        heapPush(0, &res);
    }
}