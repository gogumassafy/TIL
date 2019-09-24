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

void InitDB()
{
	
}

void Add(char* name, char* number, char* birthday, char* email, char* memo)
{

}

int Delete(FIELD field, char* str)
{
	return -1;
}

int Change(FIELD field, char* str, FIELD changefield, char* changestr)
{
	return -1;
}

RESULT Search(FIELD field, char* str, FIELD ret_field)
{
	RESULT result;
	result.count = -1;

	return result;
}