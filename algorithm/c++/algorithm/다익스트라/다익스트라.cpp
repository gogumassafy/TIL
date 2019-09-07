#include <stdio.h>
const int MAXN = 20005;
const int MAXM = 3000005;
const int inf = 1e9;
int N, M, X;
struct EDGE {
	int s, e, t;
	int prv;
} e[MAXM];
int to[MAXN];
int dist[MAXN];
struct HEAP
{
	int x, t;
} h[MAXM], htmp; int hn;
void SWAP(HEAP &a, HEAP &b) {
	htmp = a; a = b; b = htmp;
}