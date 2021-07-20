const int MAXS = (int)5e8;
const int LM = 50005;
const int SIZE = (1 << 17);
int hcnt, lcnt, N;

int strcomp(char a[], char b[]) {
	for (int i = 0; a[i] || b[i]; i++) if (a[i] != b[i]) return 0;
	return 1;
}

struct Name {
	int score[6];
	char name[13];
	Name* next;
	Name* alloc(char _name[], Name* _next) {
		int i;
		for (i = 0; _name[i]; i++) name[i] = _name[i];
		name[i] = 0; next = _next;
		return this;
	}
} hashbuf[LM], *hash[20000];

Name* search(char name[]) {
	int id = (name[0] - 'a') * 676 + (name[1] - 'a') * 26 + (name[2] - 'a');

	for (Name* p = hash[id]; p; p = p->next) {
		if (strcomp(name, p->name)) return p;
	}
	return hash[id] = hashbuf[hcnt++].alloc(name, hash[id]);
}

int tree[6][SIZE];

struct Data {
	int val;
	Data* next;
	Data* alloc(int _val, Data* _next) {
		val = _val, next = _next;
		return this;
	}
}listbuf[300000], *list[6][50010];

void update(int tree[], int node, int s, int e, int id, int mp) {
	tree[node] += mp;
	if (s == e) return;
	int m = (s + e) / 2;
	if (id <= m) update(tree, node * 2, s, m, id, mp);
	else update(tree, node * 2 + 1, m + 1, e, id, mp);
}

int count(int tree[], int node, int ts, int te, int us, int ue) {
	if (ts > ue || te < us) return 0;
	if (us <= ts && te <= ue) return tree[node];
	int m = (ts + te) / 2;
	return count(tree, node * 2, ts, m, us, ue)
		+ count(tree, node * 2 + 1, m + 1, te, us, ue);
}

void init() {
	hcnt = lcnt = N = 0;
	for (int i = 0; i < 20000; ++i) hash[i] = 0;
	for (int i = 0; i < 6; ++i) {
		for (int j = 0; j < 130000; j++) tree[i][j] = 0;
		for (int j = 0; j <= 50000; ++j) list[i][j] = 0;
	}
}

void addPlayer(char name[], int rscore[]) {
	Name* player = search(name);
	player->score[5] = 0;

	for (int i = 0; i < 5; ++i) {
		player->score[i] = rscore[i];
		player->score[5] += rscore[i];
	}

	for (int i = 0; i < 6; ++i) {
		int id = player->score[i] / 2000;
		if (i == 5) id /= 5;
		update(tree[i], 1, 0, 50000, id, 1);
		list[i][id] = listbuf[lcnt++].alloc(player->score[i], list[i][id]);
	}
}

void removePlayer(char name[]) {
	Name* player = search(name);

	for (int i = 0; i < 6; i++) {
		int id = player->score[i] / 2000;
		if (i == 5) id /= 5;
		update(tree[i], 1, 0, 50000, id, -1);
		for (Data* p = list[i][id]; p; p = p->next) {
			if (p->val == player->score[i]) {
				p->val = -1;
				break;
			}
		}
	}
}

int getRank(char name[], int index) {
	Name* player = search(name);
	
	int id = player->score[index] / 2000;
	if (index == 5) id /= 5;
	int rank = count(tree[index], 1, 0, 50000, id + 1, 50000);
	for (Data* p = list[index][id]; p; p = p->next) {
		if (p->val > player->score[index]) rank++;
	}
	return rank + 1;
}

int countPlayers(int lowScore, int highScore, int index) {
	int lowid = lowScore / 2000, highid = highScore / 2000;
	if (index == 5) lowid /= 5, highid /= 5;
	int sum = count(tree[index], 1, 0, 50000, lowid, highid);
	for (Data* p = list[index][lowid]; p; p->next) {
		if (p->val >= 0 && p->val < lowScore) sum--;
	}
	for (Data* p = list[index][highid]; p; p = p->next) {
		if (p->val > highScore) sum--;
	}
	return sum;
}