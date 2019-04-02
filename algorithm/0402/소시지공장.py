import collections

N = int(input())
raw = list(map(int, input().split()))
sausage = []
for i in range(0, len(raw), 2):
    sausage.append((raw[i], raw[i + 1]))
result = 0
while sausage:
    sausage.sort(reverse=True)
    start = sausage.pop()
    temp = collections.deque()
    while sausage:
        if sausage[-1][1] >= start[1]:
            start = sausage.pop()
        else:
            temp.appendleft(sausage.pop())
    sausage = list(temp)
    result += 1
print(result)
