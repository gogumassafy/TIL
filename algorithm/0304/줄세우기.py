N = int(input())

card = list(map(int, input().split()))
result = []

# 자기 인덱스 - 뽑은 번호 = 새로운 인덱스
for i, v in enumerate(card):
    result.insert(i-card[i], i+1)

print(*result)

