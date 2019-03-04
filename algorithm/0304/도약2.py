N = int(input())
leaf = []
distance = [0]
cnt = 0

for _ in range(N):
    leaf.append(int(input()))
leaf.sort()

shortest = leaf[1] - leaf[0]
longest = (leaf[-1] - leaf[0]) // 2 + 1
for first in range(shortest, longest):
    for i in range(len(leaf)-2):
        first_leaf = leaf[i] + first
        if first_leaf in leaf:
            for second in range(first, 2*first+1):
                second_leaf = first_leaf + second
                if second_leaf in leaf:
                    cnt += 1
                if second_leaf > leaf[-1]:
                    break
        continue
print(cnt)