import sys
sys.stdin = open('글자수_input.text')

test = int(input())

for tc in range(test):
    char = list(input())
    count_list = [0, 0]
    text = input()

    for i in range(len(char)):
        for j in text:
            if char[i] == j:
                count_list[0] += 1
        if count_list[0] > count_list[1]:
            count_list[1] = count_list[0]
        count_list[0] = 0

    print(f'#{tc+1} {count_list[1]}')