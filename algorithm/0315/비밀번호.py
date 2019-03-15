for tc in range(1, 11):
    N, raw = input().split()
    stack = []
    for i in raw:
        if stack:
            if stack[-1] == i:
                stack.pop()
                continue
        stack.append(i)
    result = ''.join(stack)
    print('#{} {}'.format(tc, result))
