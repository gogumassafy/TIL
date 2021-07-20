#include <stdio.h>

struct data {
	int num;
	data* prev, * next, * adr;
	data* alloc(int _num, data* _prev, data* _next, data* _adr) {
		num = _num, prev = _prev, next = _next, adr = _adr;
		if (prev) prev->next = this;
		if (next) next->prev = this;
		return this;
	}

	void del() {
		prev->next = next;
		if (next) next->prev = prev;
	}
} *mem[10001], *dat[40000], buf[1000000];
int cnt[40000], table[110][13], bn;

int days(int y, int m) {
	int d[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	if (y % 400 == 0 || (y % 4 == 0 && y % 100)) d[2] = 29;
	return d[m];
} 

void table_fill() {
	int i, j, y;
	for (i = 2018; i < 2118; i++) {
		y = i - 2018;
		for (j = 1; j <= 12; j++) {
			table[y][j] = table[y][j - 1] + days(i, j);
		}
		table[y + 1][0] = table[y][12];
	}
}

void init() {
	bn = 0;
	for (int i = 1; i <= 10000; i++) {
		mem[i] = buf[bn++].alloc(i, 0, 0, 0);
	}

	for (int i = 0; i < 40000; i++) {
		dat[i] = buf[bn++].alloc(i, 0, 0, 0), cnt[i] = 0;
	}
}

int encode(int y, int m, int d) {
	return table[y - 2018][m - 1] + d;
}

void push(int id, int dn) {
	cnt[dn]++;
	buf[bn].alloc(dn, mem[id], mem[id]->next, buf + bn + 1);
	buf[bn + 1].alloc(id, dat[dn], dat[dn]->next, buf + bn);
	bn += 2;
}

void del_id(int id) {
	while (mem[id]->next) {
		cnt[mem[id]->next->num]--;
		mem[id]->next->adr->del();
		mem[id]->next->del();
	}
}

void cancel() {
	int method, id, y, m, d, dn;
	scanf("%d", &method);
	if (method == 2) {
		scanf("%d", &id);
		del_id(id);
	}
	else {
		scanf("%4d%2d%2d", &y, &m, &d);
		dn = encode(y, m, d);
		while (dat[dn]->next) {
			if (method == 0) {
				cnt[dn]--;
				dat[dn]->next->adr->del();
				dat[dn]->next->del();
			}
			else del_id(dat[dn]->next->num);
		}
	}
}

void output() {
	int y, m, d, dn, sum = 0;
	scanf("%4d%2d%2d", &y, &m, &d);
	dn = encode(y, m, d);
	for (int i = 0; i < 30; i++) {
		sum += cnt[dn + i];
	}
	printf("%d\n", sum);
}

void reserve() {
	int id, method, repeat, y, m, d, dn, i;
	scanf("%d %d %d", &id, &method, &repeat);
	scanf("%4d%2d%2d", &y, &m, &d);
	dn = encode(y, m, d);
	if (method == 0) repeat = 1;
	for (i = 0; i < repeat; i++) {
		push(id, dn);
		if (method == 8) {
			if (++m > 12) y++, m = 1;
			dn = encode(y, m, d);
		}
		else if (method == 9) {
			dn = encode(++y, m, d);
		}
		else dn += method;
		if (y > 2117 || dn > table[99][12]) break;
	}
}

int main() {
	int TC, N, cmd;
	table_fill();
	scanf("%d", &TC);
	while (TC--) {
		scanf("%d", &N);
		init();
		while (N--) {
			scanf("%d", &cmd);
			switch (cmd) {
			case 1:
				reserve(); break;
			case 2:
				cancel(); break;
			case 3:
				output();
			}
		}
	}
	return 0;
}