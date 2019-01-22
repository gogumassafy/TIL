import sys
sys.stdin = open("금속막대_input.text")
test_num = int(input())

for tc in range(test_num):
    N = int(input())
    screw_list = list(map(int, input().split()))
    f_screw = [i for i in screw_list[1:2*N:2]]
    m_screw = [i for i in screw_list[0:2*N:2]]
    sort_list = []

    for i in range(N):
        if m_screw[i] not in f_screw:
            sort_list += [m_screw[i], f_screw[i]]
            break

    for i in range(1, 2*N, 2):
        for j in range(N):
            if sort_list[i] == m_screw[j]:
                sort_list += [m_screw[j], f_screw[j]]

    print(f"#{tc + 1} {' '.join(map(str, sort_list))}")



