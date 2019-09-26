#define NULL 0;

typedef enum
{
	NAME,
	NUMBER,
	BIRTHDAY,
	EMAIL,
	MEMO
} FIELD;

typedef struct
{
	int count;
	char str[20];
} RESULT;

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

const int PRIME = 1000007, BASE = 991;

int my_hash(char *str) {
	long long ret = 0;
	for (char *c = str; *c != 0; c++) {
		ret *= BASE;
		ret += *c;
		ret %= PRIME;
	}
	return ret; // 0 .. PRIME-1
}

struct LinkedList {
	int id;
	LinkedList* next;
};

struct Record {
	char* str[5];
	int hash[5];
	bool alive;
};

const int MAX_NUM_RECORDS = 50005;
Record records[MAX_NUM_RECORDS];
int num_records;

LinkedList* hash_table[5][PRIME];

void InitDB()
{
	num_records = 0;
}

void Add(char* name, char* number, char* birthday, char* email, char* memo)
{
	int id = num_records++;
	records[id] = { name, number, birthday, email, memo };
	if (hash_table[0][my_hash(name)] == 0) {

	}
	if (hash_table[1][my_hash(number)] == 0) {

	}
	if (hash_table[2][my_hash(birthday)] == 0) {

	}
	if (hash_table[3][my_hash(email)] == 0) {

	}
	if (hash_table[4][my_hash(memo)] == 0) {

	}

	// hash_table[0][my_hash(name)] <- id
	// hash_table[1][my_hash(number)] <- id
	// hash_table[2][my_hash(birthday)] <- id
	// hash_table[3][my_hash(email)] <- id
	// hash_table[4][my_hash(memo)] <- id
}

int Delete(FIELD field, char* str)
{
	// hash_table[field][my_hash(str)]
	//   --> record.alive == true && record.str == str --> record.alive = false

	return -1;
}

int Change(FIELD field, char* str, FIELD changefield, char* changestr)
{
	// hash_table[field][my_hash(str)]
	//   --> record.alive == true && record.str == str 
	//     --> record.alive = false
	//     --> new_record = record + changefield¸¸ changestr
	//         Add(new_record);

	return -1;
}

RESULT Search(FIELD field, char* str, FIELD ret_field)
{
	RESULT result;
	result.count = -1;
	// hash_table[field][my_hash(str)]
	//   --> record.alive == true && record.str == str 


	return result;
}