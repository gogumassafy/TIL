import sys
sys.stdin = open('비밀번호.txt')

for tc in range(1, 11):
    N, raw = map(str, input().split())
    stack = []
    for i in raw:
        if stack:
            if stack[-1] == i:
                stack.pop()
                continue
        stack.append(i)
    print('#{} {}'.format(tc, ''.join(stack)))


#1 1234
#2 4123
#3 123123
#4 1234123123
#5 12341
#6 123535
#7 123432141
#8 231231321
#9 12312323
#10 9823