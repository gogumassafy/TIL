M = int(input())
map_info = [list(map(int, input())) for _ in range(M)]
P = int(input())
pattern_info = [[list(map(int, input())) for _ in range(P)]]

# 회전시켜서 넣기 다만 튜플로 저장됨.
# for i in range(1, 4):
#     pattern_info.append(list(zip(*pattern_info[i-1])))
#     print(pattern_info)

# 회전 시켜서 넣기 리스트로 저장됨.
for i in range(1, 4):
    pattern_info += [[list(x) for x in zip(*pattern_info[i-1])]]
    # print(pattern_info)

cnt = 0
for i in range(M-P+1):
    for j in range(M-P+1):
        for k in range(4):
            for row in range(P):
                for col in range(P):
                    if map_info[i+row][j+col] != pattern_info[k][row][col]:
                        break
                else:
                    continue
                break
            else:
                cnt += 1
print(cnt)
