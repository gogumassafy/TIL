T = int(input())
dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
for tc in range(1, T + 1):
    n, m = input().split()
    m = int(m)
    raw = list(input().split())
    raw.sort(key=lambda x: dict[x])
    print('{} '.format(n), *raw)