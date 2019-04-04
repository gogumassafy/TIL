N, K = map(int, input().split())
raw = input()
data = list(range(N))
p = N // 4
num_list = []
for cnt in range(p):
    for i in range(4):
        each = 0
        for j in range(p):
            if raw[data[p*i + j]].isalpha():
                each += (16**(p-1-j))*(ord(raw[data[p*i + j]]) - ord('A') + 10)
            else:
                each += (16**(p-1-j))*int(raw[data[p*i + j]])
        if each in num_list:
            continue
        else:
            num_list.append(each)
    temp = data[:]
    for i in range(N):
        data[(i + 1) % N] = temp[i]
num_list.sort(reverse=True)
print(num_list[K - 1])
