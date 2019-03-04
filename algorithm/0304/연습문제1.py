import sys
sys.stdin = open('연습문제1.txt')

n, e = map(int, input().split())
input_list = list(map(int, input().split()))
result = [[i,0,0,0] for i in range(n+1)]

for i in range(0, len(input_list), 2):
    if result[input_list[i]][1]:
        result[input_list[i]][2] = input_list[i+1]
    else:
        result[input_list[i]][1] = input_list[i+1]
    result[input_list[i+1]][3] = input_list[i]

print("\n".join("{0:3d} {1:3d} {2:3d} {3:3d}".format(*result[i]) for i in range(1, len(result))))


