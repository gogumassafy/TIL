extern void query(char sector[][4]);

int N, M, map[35][35], empty;
int block[10000][2][2], chk[10000], bn;
char q[4][4];

void encode(char board[][65]) {
	for (int i = 0; i < M; i++) for (int j = 0; j < M; ++j)
		map[i][j] = 0;

	for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) {
		if (board[i][j] == '*') continue;
		map[i / 2][j / 2] = ((map[i / 2][j / 2] << 4) + (board[i][j] - 64));
	}
}

void encode(int b[2][2]) {
	for (int i = 0; i < 2; i++) for (int j = 0; j < 2; ++j)
		b[i][j] = 0;

	for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j)
		b[i / 2][j / 2] = ((b[i / 2][j / 2] << 4) + q[i][j] - 64);
}

void decode(char board[][65]) {
	for (int i = N - 3; 1 < i; i--) for (int j = N - 3; 1 < j; j--) {
		board[i][j] = ((map[i / 2][j / 2] % 16) + 64);
		map[i / 2][j / 2] >>= 4;
	}
}

int same_check(int b[2][2]) {
	for (int i = 0; i < bn; i++)
		if ((block[i][0][0] == b[0][0]) && (block[i][0][1] == b[0][1]))
			return 1;
	return 0;
}

int update(int b[2][2], int sr, int sc, int er, int ec) {
	int cnt = 0;
	
	int i = 0, j = 0;
	for (i = sr; i < er; i++) {
		for (j = sc; j < ec; j++) {
			cnt = 0;
			for (int r = 0; r < 2; r++) for (int c = 0; c < 2; c++)
				if (map[i + r][j + c] == b[r][c]) cnt++;
			if (cnt == 4) return 1;
			else if (2 <= cnt) {
				for (int r = 0; r < 2; r++) for (int c = 0; c < 2; c++) {
					if (map[i + r][j + c] == 0) {
						map[i + r][j + c] = b[r][c];
						--empty;
					}
				}
				for (int k = 0; k < bn; k++) {
					if (chk[k] == 0) {
						chk[k] = update(block[k], i - 1, j - 1, i + 2, j + 2);
					}
				}
				return 1;
			}
		}
	}
	return 0;
}

void repair(int n, int m, char board[][65])
{
	N = n, M = n / 2, bn = 0;
	empty = (M - 2) * (M - 2);
	for (int i = 0; i < 10000; i++) chk[i] = 0;
	encode(board);

	for (int i = 0; i < m; ++i) {
		query(q);
		encode(block[bn]);
		if (same_check(block[bn])) continue;
		chk[bn] = update(block[bn], 0, 0, M - 1, M - 1);
		bn++;
		if (empty * 20 <= M * M) break;
	}

	decode(board);
}