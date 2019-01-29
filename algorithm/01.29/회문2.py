import sys
sys.stdin = open('회문2_input.text')

for tc in range(10):
    # input을 받는 과정.
    N = int(input())
    input_list=[""]*100
    count_num = 1
    for row in range(100):
        input_list[row]=input()

    # row 검사하는 과정
    for M in range(100, 1, -1):
        if M <= count_num:
            break
        for row in range(100):
            for column in range(100-M+1):
                for i in range(M//2+1):
                    if input_list[row][column+i] != input_list[row][column+M-1-i]:
                        break
                else:
                    if M > count_num:
                        count_num = M

    for M in range(100, 1, -1):
        if M <= count_num:
            break
        for column in range(100):
            for row in range(100-M+1):
                for i in range(M//2+1):
                    if input_list[row+i][column] != input_list[row+M-1-i][column]:
                        break
                else:
                    if M > count_num:
                        count_num = M

    print(f'#{N} {count_num}')
