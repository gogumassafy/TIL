#include <iostream>
using namespace std;

#define MAX_NUM 300001
#define Max 300000
#define Min 0

typedef struct Node {
	bool isRed;
	int par;
	int child[2];
	long long cnt;
	Node() {
		isRed = false;
		par = 0;
		child[0] = child[1] = { 0 };
		cnt = 0;
	}
} node;


node tree[MAX_NUM];
int rootIdx = 0, N, input, bigger, smaller;
long long C = 0;


void insert(int value, int idx);
void checking(int child);
void restruct(int grand, int par, int child);
void recolor(int grand, int par, int uncle);


int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%d", &input, i);
		bigger = Max, smaller = Min;
		insert(input, rootIdx);
		C += tree[input].cnt;
		printf("%lld\n", C);
	}

	
	return 0;
}

void insert(int value, int idx) {
	if (idx == 0) {
		rootIdx = value;
		return;
	}
	if (idx > smaller && idx < value) smaller = idx;
	if (idx < bigger && idx > value) bigger = idx;

	if (idx < value) {
		if (tree[idx].child[1] != 0) {
			insert(value, tree[idx].child[1]);
		}
		else {
			tree[idx].child[1] = value;
			tree[value].par = idx;
			tree[value].isRed = true;
			if (tree[smaller].cnt > tree[bigger].cnt) tree[value].cnt = tree[smaller].cnt + 1;
			else tree[value].cnt = tree[bigger].cnt + 1;
			checking(value);
		}
	}
	else if (idx > value) {
		if (tree[idx].child[0] != 0) {
			insert(value, tree[idx].child[0]);
		}
		else {
			tree[idx].child[0] = value;
			tree[value].par = idx;
			tree[value].isRed = true;
			if (tree[smaller].cnt > tree[bigger].cnt) tree[value].cnt = tree[smaller].cnt + 1;
			else tree[value].cnt = tree[bigger].cnt + 1;
			checking(value);
		}
	}
}

void checking(int child) {
	int parent = tree[child].par,
		grandPar = tree[parent].par,
		uncle;
	if (tree[parent].isRed) {
		for (int i = 0; i < 2; ++i) {
			if (tree[grandPar].child[i] == parent) continue;
			uncle = tree[grandPar].child[i];
			if (tree[uncle].isRed) recolor(grandPar, parent, uncle);
			else restruct(grandPar, parent, child);
			break;
		}
	}
}

void restruct(int grand, int par, int child) {
	int center;
	if (grand > par) {
		// LL
		if (par > child) {
			tree[grand].child[0] = tree[par].child[1];
			tree[tree[par].child[1]].par = grand;
			tree[par].child[1] = grand;

			tree[par].par = tree[grand].par;
			tree[grand].par = par;

			tree[par].isRed = false;
			tree[grand].isRed = tree[child].isRed = true;

			center = par;
		}
		// LR
		else {
			tree[child].par = tree[grand].par;

			tree[par].child[1] = tree[child].child[0];
			tree[grand].child[0] = tree[child].child[1];
			
			tree[tree[child].child[0]].par = par;
			tree[tree[child].child[1]].par = grand;

			tree[par].par = tree[grand].par = child;
			tree[child].child[0] = par, tree[child].child[1] = grand;



			tree[child].isRed = false;
			tree[grand].isRed = tree[par].isRed = true;

			center = child;
		}
	}
	else {
		// RR
		if (child > par) {
			tree[grand].child[1] = tree[par].child[0];
			tree[tree[par].child[0]].par = grand;
			tree[par].child[0] = grand;

			tree[par].par = tree[grand].par;
			tree[grand].par = par;

			tree[par].isRed = false;
			tree[grand].isRed = tree[child].isRed = true;

			center = par;
		}
		// RL
		else {
			tree[child].par = tree[grand].par;

			tree[par].child[0] = tree[child].child[1];
			tree[grand].child[1] = tree[child].child[0];

			tree[tree[child].child[1]].par = par;
			tree[tree[child].child[0]].par = grand;

			tree[par].par = tree[grand].par = child;
			tree[child].child[1] = par, tree[child].child[0] = grand;

			tree[child].isRed = false;
			tree[grand].isRed = tree[par].isRed = true;

			center = child;
		}
	}
	if (tree[center].par == 0) {
		rootIdx = center;
		return;
	}

	for (int i = 0; i < 2; ++i) {
		if (tree[tree[center].par].child[i] != grand) continue;
		tree[tree[center].par].child[i] = center;
		break;
	}
}

void recolor(int grand, int par, int uncle) {
	tree[grand].isRed = true;
	tree[par].isRed = tree[uncle].isRed = false;
	if (tree[grand].par == 0) {
		tree[grand].isRed = false;
		return;
	}
	checking(grand);
}