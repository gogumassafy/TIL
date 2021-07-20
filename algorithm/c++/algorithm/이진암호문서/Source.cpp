#define LM 288

typedef unsigned long long LL;

int N, M;
char pdCandidate[LM][LM];

int order[5], chk[5];

LL pdCode[LM / 3][LM / 3];
LL vdSet[LM / 3][LM / 3];

void init(int docSize) {
    N = docSize;
    M = N / 2;
    for (int i = 0; i < 5; i++) 
        order[i] = chk[i] = 0;
}

void encode(char original[][LM], LL code[][LM / 3], int n) {
    int i, j;
    for (i = 0; i < n / 3; i++) {
        for (j = 0; j < n / 3; j++) {
            code[i][j] = 0;
        }
    }
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            code[i / 3][j / 3] <<= 5;
            code[i / 3][j / 3] += (original[i][j] - 'A');
        }
    }
}

int comp(int r, int c) {
    int i, j, cnt = 0;
    for (i = 0; i < M / 3; i++) {
        for (j = 0; j < M / 3; j++) {
            LL tmp = (pdCode[r + i][c + j] ^ vdSet[i][j]);
            while (tmp) {
                if (tmp & 31) cnt++;
                tmp >>= 5;
            }
            if (cnt * 20 > M * M) return 0;
        }
    }
    return 1;
}

int samecheck() {
    int i, j;
    for (i = 0; i <= M / 3; i++) {
        for (j = 0; j <= M / 3; j++) {
            if (comp(i, j)) return 1;
        }
    }
    return 0;
}

int check(char document[][LM][LM]) {
    int i, j, k, sr, sc;
    for (int k = 0; k < 4; ++k) {
        sr = k / 2 * M;
        sc = k % 2 * M;
        for (i = 0; i < M; i++) {
            for (j = 0; j < M; j++) {
                pdCandidate[sr + i][sc + j] = document[order[k]][i][j];
            }
        }
    }
    encode(pdCandidate, pdCode, LM);
    encode(document[order[4]], vdSet, M);
    if (samecheck()) {
        return 1;
    }
    return 0;
}

int dfs(int depth, char document[][LM][LM]) {
    if (depth >= 5) {
        if (check(document)) {
            return 1;
        }
    }
    else {
        for (int i = 0; i < 5; i++) {
            if (chk[i]) continue;
            chk[i] = 1;
            order[depth] = i;
            if (dfs(depth + 1, document)) return 1;
            chk[i] = 0;
        }
    }
    return 0;
}

void restorePD(int docSize, char document[][LM][LM], char repd[][LM])
{
    init(docSize);
    dfs(0, document);
    for (int i = 0; i < docSize; i++) {
        for (int j = 0; j < docSize; j++) {
            repd[i][j] = pdCandidate[i][j];
        }
    }
}