def solve(data, dumpCount):
    for i in range(dumpCount):
        maxIndex = 0        # 최고높이 인덱스
        minIndex = 0        # 최저높이 인덱스
        for j in range(1, 100):
            if data[maxIndex] < data[j]: #최고 높이의 상자 찾기
                maxIndex = j
            if data[minIndex] > data[j]: #최저 높이의 상자 찾기
                minIndex = j
        data[maxIndex] -= 1     #최고 높이 감소
        data[minIndex] += 1     #최저 높이 증가

    # 반드시 최종 덤프 수행 후, 최고점과 최저점의 높이 차 반환
    maxValue = data[0]
    minValue = data[0]
    for i in range(1, 100):
        if maxValue < data[i] : maxValue = data[i]
        if minValue > data[i] : minValue = data[i]

    return maxValue - minValue

import sys
sys.stdin = open("flatten_input.txt")
T = 10
for tc in range(T):
    dumpCount = int(input())
    data = list(map(int, input().split())) # 가로 길이는 100
    print("#{} {}".format(tc+1, solve(data, dumpCount)))