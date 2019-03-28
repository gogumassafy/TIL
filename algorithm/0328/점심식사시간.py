import queue

# 계단 이동 구조
# 1. 입구에 도착하면 1분 대기
# 2. 그 후 계단을 내려가기 시작
# 2.1. 동시에 계단 내려가는건 최대 3명까지
# 2.2. 그 외 인원은 계단 입구에서 대기
# 3. 계단을 내려가는데 걸리는 시간은 K분
# 3.1. 계단 내려가기 시작한 시간 + K 하면 이동완료 시간
# 3.2. 3.1.이 되면 바로 다음 시간이 들어감. 해당 시간에 동시에


def calc():
    for i in range(len(selected)):
        pr = people[i][0]
        pc = people[i][1]
        dr = door[selected[i]][0]
        dc = door[selected[i]][1]
        if selected[i]:
            door_one.put(abs(pr - dr) + abs(pc - dc) + 1)
        else:
            door_zero.put(abs(pr - dr) + abs(pc - dc) + 1)
    print('door_one')
    print(door_one.queue)
    print('door_zero')
    print(door_zero.queue)
    door_one.queue.clear()
    door_zero.queue.clear()
    return


def perm(n, k):
    if n == k:
        calc()
        return
    else:
        selected[k] = 1
        perm(n, k + 1)
        selected[k] = 0
        perm(n, k + 1)
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    # 사람의 숫자
    count = 0
    door = []
    people = []
    door_zero = queue.PriorityQueue()
    door_one = queue.PriorityQueue()
    for i in range(N):
        for j in range(N):
            if raw[i][j] == 1:
                count += 1
                people.append((i, j))
            if raw[i][j] > 1:
                door.append((i, j))
    selected = [0] * count
    result = 0
    perm(count, 0)
    # print('#{} {}'.format(tc, result))
