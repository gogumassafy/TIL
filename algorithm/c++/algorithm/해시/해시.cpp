#include <iostream>
using namespace std;

#define MAX_KEY 64
#define MAX_DATA 128
#define MAX_TABLE 4096

typedef struct {
	char key[MAX_KEY + 1];
	char data[MAX_DATA + 1];
} Hash;

Hash tb[MAX_TABLE];

unsigned long hash(const char *str) {
	unsigned long hash = 5381;
	int c;

	while (c = *str++) {
		hash = (((hash << 5) + hash) + c) % MAX_TABLE;
	}

	return hash % MAX_TABLE;
}


int find(const char *key, char *data) {
	unsigned long h = hash(key);
	int cnt = MAX_TABLE;

	while (tb[h].key[0] != 0 && cnt--) {
		if ()
	}
}

int main() {

	return 0;
}