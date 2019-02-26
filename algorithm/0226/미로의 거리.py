import sys
sys.stdin = open('미로의_거리.txt')

row = [1, -1, 0, 0]
col = [0, 0, 1, -1]

def BFS():
    while maze_que:
        start_row, start_col = maze_que.pop(0)
        for i in range(4):
            if N > (start_row+row[i]) > -1 and N > (start_col+col[i]) > -1:
                if not visited[start_row+row[i]][start_col+col[i]] and input_list[start_row+row[i]][start_col+col[i]] == '0':
                    visited[start_row+row[i]][start_col+col[i]] = visited[start_row][start_col] + 1
                    maze_que.append((start_row+row[i], start_col+col[i]))
                elif not visited[start_row+row[i]][start_col+col[i]] and input_list[start_row+row[i]][start_col+col[i]] == '3':
                    return visited[start_row][start_col]
    return 1


T = int(input())
for tc in range(T):
    N = int(input())
    input_list=[list(input()) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    maze_que = []
    for i in range(N):
        for j in range(N):
            if input_list[i][j] == '2':
                maze_que.append((i,j))
                visited[i][j] = 1
                distance = BFS()

    print(f'#{tc+1} {distance-1}')