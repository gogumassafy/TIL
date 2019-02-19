import sys
sys.stdin = open("Forth.txt")

T = int(input())
operator = "+-*/"

for tc in range(T):
    num_stack = []
    result = 0

    num_input = map(str, input().split())
    for i in num_input:
        if i not in operator:
            if i != ".":
                num_stack.append(int(i))
        elif len(num_stack) < 2:
            # print(f'#{tc+1} error')
            num_stack.pop()
            num_stack.append("error")
            break
        else:
            b = num_stack.pop()
            a = num_stack.pop()
            if i == "+":
                num_stack.append(a + b)
            elif i == "-":
                num_stack.append(a - b)
            elif i == "*":
                num_stack.append(a * b)
            elif i == "/":
                num_stack.append(a // b)
    if len(num_stack) > 1:
        num_stack.append("error")
    print(f'#{tc+1} {num_stack.pop()}')