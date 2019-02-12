import sys
sys.stdin = open("괄호검사_input.txt")


def isPair(string):
    bracket_stack = []
    left = "([{"
    right = ")]}"

    for i in string:
        if i in left:
            bracket_stack.append(i)
        elif i in right:
            if not len(bracket_stack):
                print(f'#{tc + 1} {0}')
                return
            elif bracket_stack[-1] == left[right.find(i)]:
                bracket_stack.pop()
            else:
                print(f'#{tc + 1} {0}')
                return
    if len(bracket_stack):
        print(f'#{tc + 1} {0}')
        return
    else:
        print(f'#{tc + 1} {1}')
        return


T = int(input())

for tc in range(T):
    bracket_stack = []
    bracket = input()
    isPair(bracket)