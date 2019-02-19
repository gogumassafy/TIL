import sys
sys.stdin = open("계산기3.txt")

for tc in range(10):
    N = int(input())
    input_string = input()
    string_stack = []
    operator_stack = []
    operator = {"+": 1,
                "*": 2}
    parentheses = "()"
    result = 0

    for i in input_string:
        if i not in operator and i not in parentheses:
            string_stack.append(i)
        elif i == "(":
            operator_stack.append(i)
        elif i == ")":
            while operator_stack[-1] != "(":
                string_stack.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while len(operator_stack) >= 1:
                if len(operator_stack) == 0 or operator_stack[-1] == "(":
                    break
            operator_stack.append(i)

    for i in range(len(operator_stack)):
        string_stack.append(operator_stack.pop())

    print(f'#{tc+1} {string_stack}')

