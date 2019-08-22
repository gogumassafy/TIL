#include <stdio.h>

using namespace std;

struct NODE {
	int prev;
	int next;
	int val;
};

const int NODE_SIZE = 30000;

const int PUSH_BACK = 0;
const int PUSH_FRONT = 1;
const int INSERT = 2;
const int POP_BACK = 3;
const int POP_FRONT = 4;
const int ERASE = 5;

int test_cmd[NODE_SIZE][3];

struct MY_LIST {
	int HEAD = NODE_SIZE;
	int TAIL = NODE_SIZE + 1;
	int pos;
	NODE node[NODE_SIZE + 2];

	MY_LIST() {
		pos = 0;
		node[HEAD].next = TAIL;
		node[TAIL].prev = HEAD;
	}
	
	void push_back(int data) {
		int prev = node[TAIL].prev;
		int next = node[prev].next;

		node[pos].val = data;
		node[pos].prev = prev;
		node[prev].next = pos;

		node[pos].next = next;
		node[next].prev = pos;
		++pos;
	}
};