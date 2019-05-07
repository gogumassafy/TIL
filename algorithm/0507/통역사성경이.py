end = '.?!'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    count = 0
    result = [0] * N
    raw = list(input().split())
    for i in raw:
        if i[0].isupper():
            if len(i) == 1:
                result[count] += 1
                continue
            for j in i[1:len(i) - 1]:
                if not j.isalpha() or j.isupper():
                    break
            else:
                if i[-1] in end or i[-1].islower():
                    result[count] += 1
        if i[-1] in end:
            count += 1
    print('#{}'.format(tc), *result)
