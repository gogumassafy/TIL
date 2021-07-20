#define MAXN 1000000
 
int Max(int a, int b) {
    return a > b ? a : b;
}

int Min(int a, int b) {
    return a > b ? b : a;
}
 
int orgLen, removeLen, userCount, start, maybe;
int arrTemp[2][MAXN];
 
extern int getNumber(int, int);
 
void init() {
    start = userCount = 0;
    for (int i = 0; i < MAXN; ++i) {
        arrTemp[0][i] = arrTemp[1][i] = -1;
    }
}
 
int binarySearch(int s, int e, int dir) {
    int m, l = s, r = e, res = -1;
 
    while (l <= r) {
        m = (l + r) / 2;
         
        if (arrTemp[dir - 1][m] == -1) {
            arrTemp[dir - 1][m] = getNumber(dir, m);
        }
 
        if (arrTemp[dir - 1][m]) {
            res = m;
            l = m + 1;
        }
        else {
            r = m - 1;
        }
    }
     
    return res;
}
 
int binarySearch2(int s, int e, int cnt) {
    int m, l = s, r = e, res = -1, orgCur, removeCur, startTemp;
 
    while (l <= r && r > start) {
        m = Max((l + r) / 2, start);
 
        if (arrTemp[0][m] == -1) arrTemp[0][m] = getNumber(1, m);
        if (arrTemp[1][m - cnt] == -1) arrTemp[1][m - cnt] = getNumber(2, m - cnt);
 
        orgCur = arrTemp[0][m], removeCur = arrTemp[1][m - cnt];
 
        if (orgCur != removeCur) {
            res = orgCur;
            r = m - 1;
            startTemp = m + 1;
        }
        else {
            l = m + 1;
        }
    }
     
    start = startTemp;
    return res;
}

int card_find(int user_ans[])
{
    init();
 
    orgLen = binarySearch(0, MAXN, 1);
    removeLen = binarySearch(Max(0, orgLen - 1000), orgLen, 2);
    userCount = orgLen - removeLen;
    maybe = orgLen / userCount * 10;
 
    for (int i = 0; i < userCount; ++i) {
        user_ans[i] = binarySearch2(start, Min(start + maybe, orgLen), i);
    }
 
    return userCount;
}