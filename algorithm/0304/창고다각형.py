# def sumArea():
#     totalArea = 0
#     start

N = int(input())
input_list = sorted([list(map(int, input().split())) for _ in range(N)])
sumArea = 0
temp = [0,0]
while 1:
    start = input_list[0]
    end = input_list[-1]
    distance = end[0] + 1 - start[0]
    minHeight = min(start[1], end[1])
    if start == end:
        sumArea += minHeight - temp[1]
        break
    sumArea += distance * (minHeight - temp[1])
    if start[1] <= end[1]:
        temp = start
        input_list = input_list[1:]
        while input_list[0][1] <= start[1] and input_list[0] != end:
            input_list = input_list[1:]
    else:
        temp = end
        input_list = input_list[:-1]
        while input_list[-1][1] <= end[1] and input_list[-1] != start:
            input_list = input_list[:-1]
print(sumArea)

