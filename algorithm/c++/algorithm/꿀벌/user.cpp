extern int moveBee(int direction[MAXBEE]);


COORD start, mybee[MAXBEE], pt[MAXBEE], bs, be, target[MAXBEE];
//리턴값, 꿀벌위치, 패턴위치, 꿀벌의 시작과 끝좌표, 목표위치

int N, Height, Width, ansd, movesum; // 최소이동거리, 이동거리 합
int order[MAXBEE], num[MAXBEE], chk[MAXBEE];
int map[105][105], visit[105][105], dir[7];
const int yy[5] = { 0,0,1,0,-1 };
const int xx[5] = { 0,1,0,-1,0 };
int Min(int x, int y) { return x < y ? x : y; }
int Max(int x, int y) { return x > y ? x : y; }
int Abs(int x) { return x < 0 ? -x : x; }

void init(int B, COORD bee[MAXBEE]) {
    N = B;
    bs.y = bs.x = 100;
    be.y = be.x = 0;
    for (int i = 0; i < N; i++) {
        mybee[i] = bee[i];
        bs.x = Min(bs.x, bee[i].x), be.x = Max(be.x, bee[i].x);
        bs.y = Min(bs.y, bee[i].y), be.y = Max(be.y, bee[i].y);
    }
}

int dfs(int sy, int sx, int n, int maxd, int sum) {
    if (maxd * 10000 + sum >= ansd * 10000 + movesum) return 0;
    int i, k, flag = 0;
    if (n >= N) {
        ansd = maxd, start = { sy,sx };
        for (i = 0; i < N; i++) order[i] = num[i];
        return 1;
    }
    for (i = 0; i < N; i++) {
        if (chk[i]) continue;
        chk[i] = 1;
        num[n] = i;
        k = Abs(pt[i].y + sy - mybee[n].y) + Abs(pt[i].x + sx - mybee[n].x);
        if (dfs(sy, sx, n + 1, Max(maxd, k), sum + k)) flag = 1;
        chk[i] = 0;
    }
    return flag;
}

void checking(int y, int x) {
    if (y<0 || y + Height >MAXSIZE || x <0 || x + Width >MAXSIZE || visit[y][x]) return;
    visit[y][x] = 1;
    for (int i = 0; i < N; i++) chk[i] = 0;
    if (!dfs(y, x, 0, 0, 0)) return;
    for (int i = 1; i <= 4; i++) {
        checking(y + yy[i], x + xx[i]);
    }
}

void setting(int h, int w) {
    int i, j, k, my, mx, sy, sx;
    my = (bs.y + be.y) / 2, mx = (bs.x + be.x) / 2;
    sy = my - h / 2, sx = mx - w / 2;
    if (sy < 0) sy = 0;
    if (sy + h > 100) sy = 100 - h;
    if (sx < 0) sx = 0;
    if (sx + w > 100) sx = 100 - w;
    for (k = 0; k < N; k++) chk[k] = 0;
    for (i = 0; i < 100; i++) for (j = 0; j < 100; j++) visit[i][j] = 0;
    checking(sy, sx);
}

int move(int k) {
    int i, j, flag = 0, ny, nx;
    for (i = 0; i < N; i++) {
        dir[i] = 0;
        for (j = 1; j <= 4; j++) {
            ny = mybee[i].y + yy[j], nx = mybee[i].x + xx[j];
            if (Abs(target[i].y - mybee[i].y) < Abs(target[i].y - ny)) continue;
            if (Abs(target[i].x - mybee[i].x) < Abs(target[i].x - nx)) continue;
            if (map[ny][nx] == k) continue;
            map[ny][nx] = k;
            dir[i] = j;
            mybee[i] = { ny,nx };
            flag = 1;
            break;
        }
    }
    return flag;
}

COORD make_pattern(int H, int W, int pattern[MAXSIZE][MAXSIZE]) {
    int i, j, k = 0;
    Height = H, Width = W;
    for (i = 0; i < 100; i++) for (j = 0; j < 100; j++) map[i][j] = 0;
    for (i = 0; i < Height; i++)for (j = 0; j < Width; j++) {
        if (pattern[i][j]) {
            pt[k++] = { i,j };
        }
    }
    ansd = movesum = 10000;
    setting(Height, Width);
    for (i = 0; i < N; i++) {
        target[i].y = pt[order[i]].y + start.y;
        target[i].x = pt[order[i]].x + start.x;
    }
    for (k = 1; move(k); k++)
        moveBee(dir);
    bs = be = start;
    be.y += Height - 1, be.x += Width - 1;
    return start;
}