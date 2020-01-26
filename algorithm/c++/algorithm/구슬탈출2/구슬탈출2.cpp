#include <iostream>
using namespace std;

#define MAX_N 1000000

typedef struct _Point {
	int br, rr;
	int bc, rc;

	_Point() {
		br = 0;
		bc = 0;
		rr = 0;
		rc = 0;
	}
	_Point(int _br, int _bc, int _rr, int _rc) {
		br = _br;
		bc = _bc;
		rr = _rr;
		rc = _rc;
	}
} Point;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

int front;
int rear;


int N, M, ans = -1;
int visited[10][10][10][10];
char input[10][10];
Point queue[MAX_N];

void bfs();
void visit(Point p);
void queueInit();
int queueIsEmpty();
int queueIsFull();
int queuePush(Point p);
int queueDequeue(Point* p);

int main() {
	queueInit();
	scanf("%d %d", &N, &M);
	Point start;
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {

		}
	}
	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < M; ++c) {
			scanf(" %c", &input[r][c]);
			if (input[r][c] == 'R') {
				start.rr = r;
				start.rc = c;
			}
			else if (input[r][c] == 'B') {
				start.br = r;
				start.bc = c;
			}
		}
	}
	queuePush(start);
	visit(start);
	bfs();
	printf("%d\n", ans);
	return 0;
}

void queueInit() {
	front = 0;
	rear = 0;
}

int queueIsEmpty() {
	return (front == rear);
}

int queueIsFull() {
	if ((rear + 1) % MAX_N == front) {
		return 1;
	}
	else {
		return 0;
	}
}

int queuePush(Point p) {
	if (queueIsFull()) {
		printf("Full");
		return 0;
	}
	else {
		queue[rear++] = p;
		return 1;
	}
}

int queueDequeue(Point* p) {
	if (queueIsEmpty()) {
		printf("Empty");
		return 1;
	}
	*p = queue[front++];
	if (front == MAX_N) {
		front = 0;
	}
	return 1;

}

void bfs() {
	int time = 0, queueCount = 0;
	Point p, goal;
	while (!queueIsEmpty()) {
		queueCount = (rear - front + MAX_N) % MAX_N;

		while (queueCount--) {
			queueDequeue(&p);
			if (input[p.rr][p.rc] == 'O') {
				ans = time;
				return;
			}
			for (int d = 0; d < 4; ++d) {
				int distance[2] = { 0, };
				int next[2][2] = { {p.br, p.bc}, {p.rr, p.rc} };
				for (int i = 0; i < 2; ++i) {
					while (input[next[i][0] + dr[d]][next[i][1] + dc[d]] != '#') {
						next[i][0] += dr[d];
						next[i][1] += dc[d];
						++distance[i];
						if (input[next[i][0]][next[i][1]] == 'O') {
							break;
						}
					}
				}

				if (input[next[0][0]][next[0][1]] == 'O') continue;
				if (next[0][0] == next[1][0] && next[0][1] == next[1][1]) {
					if (distance[0] > distance[1]) {
						next[0][0] -= dr[d];
						next[0][1] -= dc[d];
					}
					else {
						next[1][0] -= dr[d];
						next[1][1] -= dc[d];
					}
				}
				if (visited[next[0][0]][next[0][1]][next[1][0]][next[1][1]]) continue;
				goal = { next[0][0], next[0][1], next[1][0], next[1][1] };
				visit(goal);
				queuePush(goal);
			}
		}
		if (++time > 10) return;
		
	}
}

void visit(Point p) {
	visited[p.br][p.bc][p.rr][p.rc] = 1;
}