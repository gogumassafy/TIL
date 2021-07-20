#ifndef NULL
#define NULL 0
#endif

extern int add_lot();
extern void assign(int lot_num, int s, int size, int member_id);
extern void back(int lot_num, int s, int size);
extern void grow(int lot_num, int s, int size, int crop);
const int MAXLOT = 100000;

struct data {
	int lot, st, size;
	data* next;
	data* myAlloc(int _lot, int _st, int _size, data* _next) {
		lot = _lot, st = _st, size = _size, next = _next;
		return this;
	}
} buf[50000], *mem[10010];

int bcnt, memsize[10010];

void push(int id, int lot, int st, int size) {
	mem[id] = buf[bcnt++].myAlloc(lot, st, size, mem[id]);
}

void move(int s, int e) {
	data* tmp = mem[s];
	mem[s] = mem[s]->next;
	tmp->next = mem[e];
	mem[e] = tmp;
}


void init_member()
{
	bcnt = 0;
	for (int i = 0; i <= 10000; i++) {
		mem[i] = 0, memsize[i] = 0;
	}
}

void assign_member(int id, int size)
{
	if (memsize[0] < size) {
		int lot = add_lot();
		push(0, lot, 0, MAXLOT);
		memsize[0] += MAXLOT;
	}
	memsize[0] -= size;
	memsize[id] = size;

	while (size > 0) {
		if (mem[0]->size > size) {
			push(0, mem[0]->lot, mem[0]->st, size);
			mem[0]->next->st += size, mem[0]->next->size -= size;
		}
		size -= mem[0]->size;
		assign(mem[0]->lot, mem[0]->st, mem[0]->size, id);
		move(0, id);
	}
}

void back_member(int id)
{
	memsize[0] += memsize[id];
	memsize[id] = 0;
	while (mem[id]) {
		back(mem[id]->lot, mem[id]->st, mem[id]->size);
		move(id, 0);
	}
}

void grow_member(int id, int crop)
{
	for (data* p = mem[id]; p; p = p->next) {
		grow(p->lot, p->st, p->size, crop);
	}
}

