n = int(input())
input_list = [input().split() for _ in range(n)]
input_list.sort(key=lambda a: int(a[0]))
min_num = float('inf')
answer = "F"
for i in input_list:
    if i[1] == "Y" and min_num > int(i[0]):
        min_num = int(i[0])
        answer = i[0]
    elif i[1] == "N" and min_num <= int(i[0]):
        answer = "F"
        break
print(answer)