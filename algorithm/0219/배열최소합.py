import sys
sys.stdin = open("배열최소합.txt")

def find_sum(row, set_sum):
    global min_sum
    if row == N:
        if min_sum > set_sum:
            min_sum = set_sum
        return
    if set_sum > min_sum:
        return

    for i in range(N):
        if a[i] == 1:
            continue
        else:
            a[i] = 1
            find_sum(row+1, set_sum + input_list[row][i])
            a[i] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    input_list = [list(map(int, input().split())) for _ in range(N)]
    a =[0] * N
    min_sum = float("inf")
    set_sum = 0
    find_sum(0, set_sum)
    print(f'#{tc+1} {min_sum}')
