K = int(input())
sol = []
for i in range(6):
    k, v = map(int, input().split())
    sol.append(v)
idx = sol.index(max(sol))
if sol[idx - 1] > sol[(idx + 1) % 6]:
    min_num = sol[(idx + 1) % 6]
    flag = 1
else:
    min_num = sol[idx - 1]
    flag = 0
h = max(sol[idx - 1], sol[(idx + 1) % 6])
sum_area = sol[idx] * h
if flag:
    sum_area -= sol[(idx + 2) % 6] * sol[(idx + 3) % 6]
else:
    sum_area -= sol[idx - 2] * sol[idx - 3]
print(sum_area*K)
