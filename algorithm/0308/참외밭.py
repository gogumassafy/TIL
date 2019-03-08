K = int(input())
sol = []
for i in range(6):
    k, v = map(int, input().split())
    sol.append(v)
idx = sol.count(max(sol))
min_num = min(sol[(idx - 1)%6], sol[(idx + 1)%6])
