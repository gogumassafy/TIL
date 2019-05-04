def solution(problems):
    for i, problem in enumerate(problems):
        N, M, K, arr = problem
        remain = simulate(N, M, K, arr)

        print('#{} {}'.format(i + 1, remain))


# 해당 문제에 대하여 simulate, return # of cells
def simulate(N, M, K, ARR):
    live_cells = []
    arr = [0] * (2 * K + N)
    # 상하좌우 K개의 padding
    for i in range(2 * K + N):
        row = [0] * (2 * K + M)
        arr[i] = row

    # 초기 상태 설정
    for i in range(N):
        for j in range(M):
            X = ARR[i][j]
            if X != 0:
                arr[K + i][K + j] = X
                live_cells.append((K + i, K + j, X, X, 2 * X))  # (x, y, X, active, dead)

    time = 0

    # print('initial--------------------------------------')
    # print('live_cells:')
    # for cell in live_cells :
    #   print(cell)
    # print('map:')
    # for row in arr :
    #   print_arr(row)

    while time < K:
        time += 1
        candidates = []  # (x, y, X, active시작, dead시작)
        for cell in live_cells:
            x, y, X, t1, t2 = cell
            # 번식
            if t1 + 1 == time:
                if arr[x][y + 1] == 0:
                    candidates.append((x, y + 1, X, time + X, time + 2 * X))
                if arr[x][y - 1] == 0:
                    candidates.append((x, y - 1, X, time + X, time + 2 * X))
                if arr[x - 1][y] == 0:
                    candidates.append((x - 1, y, X, time + X, time + 2 * X))
                if arr[x + 1][y] == 0:
                    candidates.append((x + 1, y, X, time + X, time + 2 * X))

        live_cells = remove_dead(live_cells, time)
        winners = get_winners(candidates)
        live_cells.extend(winners)
        # map에 반영
        for item in winners:
            x, y, X, t1, t2 = item
            arr[x][y] = X

        # print('--------------------after time: ', time)
        # print('candidates: ', candidates)
        # print('winners: ', winners)
        # print('# live cells: ', len(live_cells))
        # for row in arr :
        #   print_arr(row)

    return len(live_cells)


# 후보들 중 X(생명력)이 가장 큰 승리자들을 return
def get_winners(candidates):
    result = []
    dic = {}
    for cand in candidates:
        x, y, X, t1, t2 = cand
        if (x, y) not in dic or dic[(x, y)][2] < X:
            dic[(x, y)] = cand

    for key in dic:
        result.append(dic[key])

    return result


# live_cells -> 죽은거 제외한 cells를 return
def remove_dead(live_cells, time):
    result = []
    for cell in live_cells:
        x, y, X, t1, t2 = cell
        if time < t2:
            result.append(cell)

    return result


# 자리수 맞추어 출력
def print_arr(arr):
    for item in arr:
        print(str(item).rjust(1), end=' ')

    print(' ')
    return


if __name__ == '__main__':
    T = int(input())
    problems = [0] * T
    for i in range(T):
        N, M, K = [int(x) for x in input().split(' ')[:3]]
        arr = [0] * N
        for j in range(N):
            row = [int(x) for x in input().split(' ')[:M]]
            arr[j] = row

        problems[i] = (N, M, K, arr)

    solution(problems)