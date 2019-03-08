N, raw = input().split()
N = int(N)
raw = list(raw)
cnt = 0
string = ''
tree = [[] for _ in range(51)]
string = ""
while raw:
    v = raw.pop(0)
    if v == "<":
        if string:
            tree[cnt].append(string)
            string = ""
        cnt += 1
    elif v == ">":
        cnt -= 1
    else:
        string += v
print(*tree[N])


