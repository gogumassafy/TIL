import sys
sys.stdin = open('로마숫자만들기.txt')
# 로마 숫자를 오름차순으로 배치하여 로마자 자체에는 중복이 없게한다.
# 하지만 이를 우리가 쓰는 아라비아 숫자로 변환하는 과정에서 필연적으로 중복이 발생하게 된다.

def count(idx, n):
    cnt = 0
    if not n:
        return 1
    for i in range(idx, 4):
        cnt += count(i, n - 1)
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    sol = count(0, N)
    print(sol)
