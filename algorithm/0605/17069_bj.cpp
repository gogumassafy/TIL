#include <stdio.h>
#include <queue>
using namespace std;

struct Node {
    // 대각선, 세로, 가로
    int dir, r, c;
};

const int dr[] = {1, 1, 0};
const int dc[] = {1, 0, 1};
int N, count = 0;
int arr[16][16];

queue<Node> q;

int bfs() {
    while(!q.empty()){
        Node value = q.front();
        int dir = value.dir;
        int r = value.r;
        int c = value.c;
        q.pop();
        if (r == N - 1 && c == N - 1) {
            count++;
            continue;
        }
        for (int i = 0; i < 3; ++i) {
            if (i*dir == 2)
                continue;
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (r >= N || r < 0 || c >= N || c < 0)
                continue;
            if (arr[nr][nc])
                continue;
            if (i == 0) {
                if (arr[nr][nc] || arr[nr - 1][nc] || arr[nr][nc - 1]) {
                    continue;
                }
            }
            q.push({i, nr, nc});
        }
    }
    return count;
}

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i){
        for (int j = 0; j < N; ++j){
            scanf("%d", &arr[i][j]);
        }
    }
    q.push({2, 0, 1});
    printf("%d", bfs());
    return 0;
}