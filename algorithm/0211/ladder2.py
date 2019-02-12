import sys

sys.stdin = open("ladder_input.txt")

ladder = [[] for _ in range(100)]

def gotostart(row, column):
        while(row > 0):
            if column != 0 and ladder[row][column - 1] == 1:

            elif column != 99 and ladder[row][column + 1] == 1:
            else:
                row -= 1
        return column


def goRight(row, column):
    column = ladder[row][column:]. - 1
    row -= 1

def goLeft(row, column):
    column = ladder[row][column::-1].index(0) + 1
    row -= 1


for tc in range(10):
    tc_num = int(input())
    for i in range(100):
        ladder[i] = list(map(int, input().split()))
    goal = ladder[99].index(2)

    print(f'#{tc_num} {gotostart(99, goal)}')
