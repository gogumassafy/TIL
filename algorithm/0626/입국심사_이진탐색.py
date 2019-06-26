def calc(time):
    global N, M
    temp = 0
    for i in range(N):
        temp += time // desk[i]
    return temp >= M


N, M = map(int, input().split())
desk = []
for i in range(N):
    time = int(input())
    desk.append(time)
desk.sort()
minTime = 0
maxTime = desk[-1] * M
while minTime < maxTime:
    midTime = (minTime + maxTime) // 2
    if calc(midTime):
        maxTime = midTime
    else:
        minTime = midTime + 1
print(minTime)
