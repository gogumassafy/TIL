import sys
sys.stdin = open('회문_input.text')

test = int(input())

for tc in range(test):
    # input을 받는 과정. 8~12
    N, M = map(int, input().split())
    input_list=[""]*N

    for row in range(N):
        input_list[row]=input()

    # row 검사하는 과정
    for row in range(N): # input 값의 row
        for column in range(N-M+1): # column, 이 for문의 의미는 시작하는 열을 의미한다. 시작은 0부터 열이 M보다 작아지기전까지 진행한다.
            for i in range(M//2+1): # 구하고자 하는 열의 절반만 비교하면 된다.
                if input_list[row][column+i] != input_list[row][column+M-1-i]: # 현재 인풋[현재 행][시작 열 + 검사가 진행중인 열] != 인풋[현재 행][시작 열에서 M만큼 떨어진 위치 - 역순으로 검사 진행]
                    break
            else:
                print(f'#{tc+1} {"".join(input_list[row][column:column+M])}')
    else:
        for column in range(N):
            for row in range(N-M+1):
                for i in range(M//2+1):
                    if input_list[row + i][column] != input_list[row + M - 1 - i][column]:
                        break
                else:
                    print(f'#{tc + 1}', end=' ')
                    for i in range(M):
                        print(f'{input_list[row+i][column]}', end='')
                    print()