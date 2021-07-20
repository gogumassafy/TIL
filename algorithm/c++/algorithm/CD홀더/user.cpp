#ifndef NULL
#define NULL 0
#endif

const int LM = 100005;
const int SIZE = (1 << 18);
int N, H, D, que[LM], chk[LM], fr, re;

struct Data {
	int max, min;
} tree[SIZE];

int Max(int x, int y) { return x > y ? x : y; }
int Min(int x, int y) { return x < y ? x : y; }

void update(int node, int s, int e, int id, int type) {
	if (s == e) {
		if (type) tree[node] = { id, id };
		else tree[node] = { -1, N };
		return;
	}

	int l = node * 2, r = l + 1, m = (s + e) / 2;
	if (id <= m) update(l, s, m, id, type);
	else update(r, m + 1, e, id, type);
	tree[node] = { Max(tree[l].max, tree[r].max), Min(tree[l].min, tree[r].min) };
}

int maxfind(int node, int s, int e, int qs, int qe) {
	if (qe < s || e < qs) return -1;
	if (qs <= s && e <= qe) return tree[node].max;
	int l = node * 2, r = l + 1, m = (s + e) / 2;
	return Max(maxfind(l, s, m, qs, qe), maxfind(r, m + 1, e, qs, qe));
}

int minfind(int node, int s, int e, int qs, int qe) {
	if (qe < s || e < qs) return N;
	if (qs <= s && e <= qe) return tree[node].min;
	
	int l = node * 2, r = l + 1, m = (s + e) / 2;
	return Min(minfind(l, s, m, qs, qe), minfind(r, m + 1, e, qs, qe));
}

void init(int holder_size, int head) {
	N = holder_size, H = head, D = 0, fr = re = 0;
	for (int i = 0; i <= N; ++i) chk[i] = 0;
	for (int i = 0; i < SIZE; ++i) tree[i] = { -1, N };
}

void insert(int holder) {
	chk[holder] = 1;
	que[re++] = holder;
	update(1, 0, N - 1, holder, 1);
}

int delid(int id) {
	chk[id] = 0;
	update(1, 0, N - 1, id, 0);
	H = id;
	return id;
}

int first() {
	while (chk[que[fr]] == 0) fr++;
	int id = que[fr++];
	return delid(id);
}

int near() {
	int lid = maxfind(1, 0, N - 1, 0, H);
	int id = minfind(1, 0, N - 1, H, N - 1);
	if (id == N || (lid >= 0 && H - lid <= id - H)) id = lid;
	return delid(id);
}

int forward() {
	int id;
	if (D == 0) id = maxfind(1, 0, N - 1, 0, H);
	else id = minfind(1, 0, N - 1, H, N - 1);
	if (id < 0 || id >= N) {
		D = 1 - D;
		if (D == 0) id = maxfind(1, 0, N - 1, 0, H);
		else id = minfind(1, 0, N - 1, H, N - 1);
	}
	return delid(id);
}

int left() {
	int id = maxfind(1, 0, N - 1, 0, H);
	if (id < 0) id = maxfind(1, 0, N - 1, 0, N - 1);
	return delid(id);
}

int right() {
	int id = minfind(1, 0, N - 1, H, N - 1);
	if (id >= N) id = minfind(1, 0, N - 1, 0, N - 1);
	return delid(id);
}