import sys
sys.stdin = open("반복문자_지우기.txt")

T = int(input())

for tc in range(T):
    input_string = input()
    string_stack = []
    for i in range(len(input_string)):
        string_stack.append(input_string[i])
        if len(string_stack) > 1 and string_stack[-2] == string_stack[-1]:
            string_stack.pop()
            string_stack.pop()

    print(f'#{tc+1} {len(string_stack)}')