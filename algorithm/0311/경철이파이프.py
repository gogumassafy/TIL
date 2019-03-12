import time, sys
start_time = time.time()
sys.stdin = open('파이프.txt')

dx = [1, 0, 1]
dy = [0, 1, 1]
ans = 0


def __dfs(arr, x, y, m):
    global ans
    n = len(arr)
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if x == n - 1 and y == n - 1:
        ans += 1
        return
    for i in range(3):
        if (m == 1 and i == 0) or (m == 0 and i == 1):
            continue
        ny = y + dy[i]
        nx = x + dx[i]
        if i == 2:
            flag = True
            for j in range(3):
                if 0 <= y + dy[j] < n and 0 <= x + dx[j] < n and arr[y + dy[j]][x + dx[j]]:
                    flag = False
            if flag:
                __dfs(arr, nx, ny, i)
        else:
            if 0 <= ny < n and 0 <= nx < n and not arr[ny][nx]:
                __dfs(arr, nx, ny, i)


def solution(n, arr):
    __dfs(arr, 1, 0, 0)


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    solution(n, arr)
    print("답:" + str(ans))


if __name__ == '__main__':
    main()