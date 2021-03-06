#include <stdio.h>
using namespace std;

struct Record {
	char* str[5];
	int hash[5];
	bool alive;
};

const int PRIME = 1000007, BASE = 991;
const int MAX_NUM_RECORDS = 50005;
Record records[MAX_NUM_RECORDS];
int num_records = 0;

void Add(char* name, char* number, char* birthday, char* email, char* memo)
{
	int id = num_records++;
	printf("%s", name);
	// records[id].str = {name, number, birthday, email, memo};

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