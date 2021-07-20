typedef unsigned long long ULL;
const int LM = 1 << 8;
int N, M, sdcnt, order[6], chk[6];
char PD[LM][LM], SD[5][LM][LM], left[LM][LM], right[LM][LM];
ULL PD64[LM / 8][LM / 8], D64[LM / 8][LM / 8];

void userInit(int docSize) {
    N = docSize;
    M = N / 2;
    sdcnt = 0;
    for (int i = 0; i < 5; i++) order[i] = chk[i] = 0;
}

int compare(int r, int c, int k) {
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            if (PD[r + i][c + j] != SD[k][i][j]) return 0;
        }
    }
    return 1;
}

int check() {
    int i, j, k, sr, sc;
    for (int k = 0; k < 4; ++k) {
        sr = k / 2 * M;
        sc = k % 2 * M;
        for (i = 0; i < M; i++) for (j = 0; j < M; ++j) {
            PD[sr + i][sc + j] = SD[order[k]][i][j];
        }
    }
    for (i = 2; i < M - 2; ++i) for (j = 2; j < M - 2; j++) {
        if (compare(i, j, order[4])) return 1;
    }
    return 0;
}

void encode(char pd[][LM], ULL pd64[][LM / 8], int n) {
    int i, j;
    for (i = 0; i < n / 8; i++) for (j = 0; j < n / 8; j++) pd64[i][j] = 0;
    for (i = 0; i < n; ++i) for (j = 0; j < n; ++j)
        pd64[i / 8][j / 8] = (pd64[i / 8][j / 8] << 1) + pd[i][j];
}

int dfs(int n) {
    if (n > 4) {
        if (check()) {
            encode(PD, PD64, LM);
            return 1;
        }
    }
    for (int i = 0; i < 5; i++) {
        if (chk[i]) continue;
        chk[i] = 1;
        order[n] = i;
        if (dfs(n + 1)) return 1;
        chk[i] = 0;
    }
    return 0;
}

void shuffledVDSD(char document[][LM]) {
    for (int i = 0; i < M; i++) for (int j = 0; j < M; j++)
        SD[sdcnt][i][j] = document[i][j];
    if (++sdcnt == 5) dfs(0);
}

int comp(int r, int c) {
    int i, j, cnt = 0;
    for (i = 0; i < M / 8; i++) for (j = 0; j < M / 8; j++) {
        ULL tmp = (PD64[r + i][c + j] ^ D64[i][j]);
        while (tmp) cnt++, tmp &= (tmp - 1);
        if (cnt * 20 > M* M) return 0;
    }
    return 1;
}

int samechk() {
    int i, j;
    for (i = 0; i <= M / 8; i++) for (j = 0; j <= M / 8; j++) {
        if (comp(i, j)) return 1;
    }
    return 0;
}

int verifyDocument(char document[][LM]) {
    for (int i = 0; i < M; ++i) for (int j = 0; j < M; ++j) {
        left[i][j] = document[M - 1 - j][i];
        right[i][j] = document[j][M - 1 - i];
    }
    encode(document, D64, M); if (samechk()) return 1;
    encode(left, D64, M); if (samechk()) return 1;
    encode(right, D64, M); if (samechk()) return 1;
    return 0;
}