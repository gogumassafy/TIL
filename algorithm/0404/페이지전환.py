N = int(input())
D = [[float('inf')] * 500 for _ in range(500)]
start_max = 0
end_max = 0
for i in range(N):
    s, e = map(int, input().split())
    if s > start_max:
        start_max = s
    if e > end_max:
        end_max = e
    D[s][e] = 1

for start in range(1, start_max + 1):
    for end in range(1, end_max + 1):
        if D[start][end] != float('inf'):
            for row in range(1, start_max + 1):
                if D[row][start] != float('inf') and end != row:
                    D[row][end] = min(D[row][end], D[row][start] + D[start][end])

count = 0
nsum = 0
for start in range(1, start_max + 1):
    for end in range(1, end_max + 1):
        if start != end:
            if D[start][end] != float('inf'):
                count += 1
                nsum += D[start][end]
print('{:.3f}'.format(nsum / count))
