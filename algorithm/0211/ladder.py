import sys

sys.stdin = open("ladder_input.txt")
# sys.stdin = open("input.txt")

ladder = [[] for _ in range(100)]


def gotostart(row, column):
        while(row > 0):
            if column != 0 and ladder[row][column - 1] == 1:
                while(column != 0 and ladder[row][column - 1] != 0):
                    column -= 1
                row -= 1
            elif column != 99 and ladder[row][column + 1] == 1:
                while (column != 99 and ladder[row][column + 1] != 0):
                    column += 1
                row -= 1
            else:
                row -= 1
        return column

for tc in range(10):
    tc_num = int(input())
    for i in range(100):
        ladder[i] = list(map(int, input().split()))
    goal = ladder[99].index(2)

    print(f'#{tc_num} {gotostart(99, goal)}')
