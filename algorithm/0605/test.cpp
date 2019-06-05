#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;

struct Node{
    int depth, rr, rc, br, bc;
};

const int dr[] = {-1, 1, 0, };
const int dc[] = {0, 0, -1, 1};
char arr[11][11];

int bfs() {
    while(!q.empty()) {
        int depth = q.front().depth;
        int rr = q.front().rr;
        int rc = q.front().rc;
        int br = q.front().br;
        int bc = q.front().bc;
        q.pop();
        if (depth == 10){
            return -1;
        }
        for (int i = 0; i < 4; ++i) {
            nrr = rr + dr[i];
            nrc = rc + dc[i];
            nbr = br + dr[i];
            nbc = bc + dc[i];
            if ()
        }
    }
    return -1;
}

int main() {
    int N, M, srr, src, sbr, sbc;
    scanf("%d %d", &N, &M);
    for(int i = 0; i < N; ++i) {
        scanf("%s", arr[i]);
        for (int j = 0; j < M; ++j){
            if (arr[i][j] == 'B') {
                sbr = i;
                sbc = j;
            }
            else if (arr[i][j] == 'R') {
                srr = i;
                src = j;
            }
        }
    }
    queue<Node> q;
    q.push({0, srr, src, sbr, sbc});
    printf("%d", bfs());
    return 0;
}