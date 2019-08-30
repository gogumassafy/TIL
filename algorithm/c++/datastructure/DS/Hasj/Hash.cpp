#include <stdio.h>
#include <map>

using namespace std;

const int PN = 23;
const int HASH_SIZE = 10000;

int table[HASH_SIZE][50];
int hash_size = 0;
char hash_raw[30000][100];

char input[30000][100];
map<char*, int> test;

