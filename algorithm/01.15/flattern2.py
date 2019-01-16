import sys

sys.stdin = open("flattern_input.txt")

T = 10

for tc in range(T):
    num = int(input())
    tower = list(map(int, input().split()))
    for _ in range(num):
        tower_height = [-float("inf"), float("inf")]  # (max, min)
        tower_index = [0, 0]  # (max, min)

        tower_index[0] = [i for i in range(len(tower)) if tower[i] > tower_height[0]]
        tower_height[0] = tower_height[tower_index[0]]

        tower_index[1] = [i for i in range(len(tower)) if tower[i] < tower_height[0]]
        tower_height[1] = tower_height[tower_index[1]]

        tower[tower_index[0]] -= 1
        tower[tower_index[1]] += 1

    if tower_height[0] not in tower:
        tower_height[0] -= 1
    if tower_height[1] not in tower:
        tower_height[1] += 1
    if tower_height[0] <= tower_height[1] + 1:
        break
    print(f"#{tc + 1} {tower_height[0] - tower_height[1]}")
