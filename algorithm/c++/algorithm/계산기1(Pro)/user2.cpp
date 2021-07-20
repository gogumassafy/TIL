#define MAXL (50 + 5)
char sol[MAXL], tmp[MAXL], num[MAXL];
int sign, ptr, mdflag;

inline void strcopy(char* dst, const char* src)
{
	for (register int i = 0; dst[i] = src[i]; i++);
}

inline void strncopy(char* dst, char* src, int len)
{
	for (register int i = 0; i < len; i++) dst[i] = src[i]; dst[len] = 0;
}

inline int strlength(char* a)
{
	register int i; for (i = 0; a[i]; i++); return i;
}

inline int strcompare(char* a, char* b)
{
	register int i; for (i = 0; a[i] && b[i] && (a[i] == b[i]); i++); return a[i] - b[i];
}

inline int conv(int* A, char* a)
{
	register int i; for (i = 0; a[i]; i++) A[i] = a[i] - '0'; return i;
}

int compare(char* a, char* b)
{
	int alen = strlength(a), blen = strlength(b);
	if (alen == blen) return strcompare(a, b);
	return alen - blen;
}

char d2c[] = "0123456789";
void mul(char* a, char* b)
{
	if ((a[0] == '0') || (b[0] == '0'))
	{
		strcopy(a, "0"); return;
	}
	int A[60], B[60], sol[120] = { 0 }; register int i, j;
	int alen = conv(A, a), blen = conv(B, b), len = alen + blen - 1;
	for (i = 0; i < alen; i++) for (j = 0; j < blen; j++)
	{
		sol[i + j] += A[i] * B[j];
	}
	for (i = len - 1; i > 0; i--)
	{
		if (sol[i] >= 10)
		{
			sol[i - 1] += sol[i] / 10; sol[i] %= 10;
		}
	}
	if (sol[0] >= 10)
	{
		a[0] = d2c[sol[0] / 10]; sol[0] %= 10; i = 1;
	}
	else i = 0;
	for (j = 0; j < len; i++, j++) a[i] = d2c[sol[j]];
	a[i] = 0;
}

inline bool divsub(int* a, int* b, int len)
{
	register int i;
	for (i = 0; i < len; i++)
	{
		if (a[i] > b[i]) break;
		if (a[i] < b[i]) return false;
	}
	for (i = len - 1; i >= 0; i--)
	{
		a[i] -= b[i];
		if (a[i] < 0)
		{
			a[i - 1]--; a[i] += 10;
		}
	}
	return true;
}

void div(char* a, char* b)
{
	if (compare(a, b) < 0)
	{
		strcopy(a, "0"); return;
	}
	int A[60], B[60], sol[60]; register int i, j;
	int alen = conv(A, a), blen = conv(B, b), len = alen - blen + 1;
	for (i = 0; i < len; i++)
	{
		sol[i] = 0;
		while (divsub(&A[i], B, blen)) sol[i]++;
		A[i + 1] += A[i] * 10; A[i] = 0;
	}
	for (i = 0, j = sol[0] == 0; j < len; i++, j++)
	{
		a[i] = d2c[sol[j]];
	}
	a[i] = 0;
}

inline void save(char* a, int* A, int len)
{
	register int i, j;
	for (i = 0; (i < len - 1) && !A[i]; i++);
	for (j = 0; i < len; i++, j++) a[j] = d2c[A[i]];
	a[j] = 0;
}

void add(char* a, char* b)
{
	int A[60] = { 0 }, B[60] = { 0 }, sol[60] = { 0 }; register int i, j;
	int alen = strlength(a), blen = strlength(b), len = (alen > blen) ? alen + 1 : blen + 1;
	for (i = len - 1, j = alen - 1; j >= 0; i--, j--) A[i] = a[j] - '0';
	for (i = len - 1, j = blen - 1; j >= 0; i--, j--) B[i] = b[j] - '0';
	for (i = len - 1; i >= 0; i--)
	{
		A[i] += B[i];
		if (A[i] >= 10)
		{
			A[i - 1]++; A[i] -= 10;
		}
	}
	save(a, A, len);
}

void sub(char* a, char* b)
{
	int A[60] = { 0 }, B[60] = { 0 }, sol[60] = { 0 }; register int i, j;
	int alen = strlength(a), blen = strlength(b), len = (alen > blen) ? alen + 1 : blen + 1;
	for (i = len - 1, j = alen - 1; j >= 0; i--, j--) A[i] = a[j] - '0';
	for (i = len - 1, j = blen - 1; j >= 0; i--, j--) B[i] = b[j] - '0';
	for (i = len - 1; i >= 0; i--)
	{
		A[i] -= B[i];
		if (A[i] < 0)
		{
			A[i - 1]--; A[i] += 10;
		}
	}
	save(a, A, len);
}

void Cal(char ch, char* user)
{
	int flag;
	if (ch == 'C')
	{
		sign = 1; ptr = 0; mdflag = 1; strcopy(sol, "0"); strcopy(tmp, "1");
		strcopy(user, "0");
	}
	else
	{
		if (('0' <= ch) && (ch <= '9'))
		{
			num[ptr++] = ch; strncopy(user, num, ptr);
		}
		else
		{
			if (ptr == 0)
			{
				strcopy(num, "0"); flag = 1;
			}
			else
			{
				num[ptr] = 0; ptr = 0; flag = 0;
			}

			if (mdflag) mul(tmp, num);
			else div(tmp, num);

			if (ch == '/')
			{
				mdflag = 0;
				if (flag)
				{
					strcopy(tmp, sol); strcopy(sol, "0");
				}
				strcopy(user, tmp);
			}
			else
			{
				mdflag = 1;
				if (ch == '*')
				{
					if (flag)
					{
						strcopy(tmp, sol); strcopy(sol, "0");
					}
					strcopy(user, tmp);
				}
				else
				{
					if (sign < 0) sub(sol, tmp);
					else add(sol, tmp);
					if (ch == '-') sign = -1;
					else sign = 1;
					strcopy(user, sol);
					strcopy(tmp, "1");
				}
			}
		}
	}
}