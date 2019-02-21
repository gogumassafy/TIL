# 숫자카드.py


import sys
sys.stdin = open("숫자카드_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    C = [0] * 10            # 카운팅배열
    N = int(input())        # 카드장수
    data = input()          # 문자열로 받음

    for i in range(N):
        C[int(data[i])] += 1    #문자열에 있는 문자를 하나씩 숫자로 변환하여 카운팅

    maxIndex = 0               #리스트의 인덱스이므로 -1로 초기화
    maxValue = C[0]
    for i in range(1, 10):
        if maxValue <= C[i]:#개수가 같은 경우 더 큰 숫자카드 찾기
            maxValue = C[i]
            maxIndex = i

    print("#{0} {1} {2}".format(test_case, maxIndex, maxValue))