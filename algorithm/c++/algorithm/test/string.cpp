#include <stdio.h>
using namespace std;

struct LinkedList {
	int id;
	LinkedList* next;
};

struct Record {
	char* str[5];
	int hash[5];
	bool alive;
};

LinkedList hash_table[5][PRIME];

const int PRIME = 1000007, BASE = 991;
const int MAX_NUM_RECORDS = 50005;
Record records[MAX_NUM_RECORDS];
int num_records = 0;



void Add(char* name, char* number, char* birthday, char* email, char* memo)
{
	int id = num_records++;
	records[id] = { name, number, birthday, email, memo };
	if (hash_table[0][my_hash(name)] == NULL) {

	}
	printf("%s", records[id].str[1]);
	//records[id].str[0] = name;
	//records[id].str[1] = number;
	//records[id].str[2] = birthday;
	//records[id].str[3] = email;
	//records[id].str[4] = memo;

	// hash_table[0][my_hash(name)] <- id
	// hash_table[1][my_hash(number)] <- id
	// hash_table[2][my_hash(birthday)] <- id
	// hash_table[3][my_hash(email)] <- id
	// hash_table[4][my_hash(memo)] <- id
}

int my_hash(char *str) {
	long long ret = 0;
	for (char *c = str; *c != 0; c++) {
		ret *= BASE;
		ret += *c;
		ret %= PRIME;
	}
	return ret; // 0 .. PRIME-1
}


int main() {
	Add("A", "111", "0101", "a.com", "aaa");
	return 0;
}