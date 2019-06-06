import sys
sys.stdin = open('색종이붙이기.txt')
papers = [5] * 5


def dfs(count, sr):
    global total, result
    if count >= result:
        return
    if total == 0:
        result = min(result, count)
        return
    for r in range(sr, 10):
        for c in range(10):
            if raw[r][c]:
                break
        else:
            continue
        break

    for i in reversed(range(5)):
        if papers[i] == 0:
            continue
        if wall(r, c, i):
            continue
        papers[i] -= 1
        total -= (i + 1)**2
        cover(r, c, i)
        dfs(count + 1, r)
        papers[i] += 1
        cover(r, c, i)
        total += (i + 1) ** 2



def wall(r, c, depth):
    for nr in range(r, r + depth + 1):
        for nc in range(c, c + depth + 1):
            if not (10 > nr >= 0 and 10 > nc >= 0):
                return 1
            if raw[nr][nc] == 0:
                return 1
    return 0


def cover(r, c, depth):
    for nr in range(r, r + depth + 1):
        for nc in range(c, c + depth + 1):
            if raw[nr][nc]:
                raw[nr][nc] = 0
            else:
                raw[nr][nc] = 1


raw = [list(map(int, input().split())) for _ in range(10)]
result = float('inf')
total = sum(sum(count) for count in raw)
if total == 0:
    print(0)
else:
    dfs(0, 0)
    if result == float('inf'):
        print(-1)
    else:
        print(result)