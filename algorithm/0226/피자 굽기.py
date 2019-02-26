import sys
sys.stdin = open('피자_굽기.txt')

def isFull():
    global front, rear, N
    if (rear + 1) % (N+1) == front:
        return True
    return False

def isEmpty():
    global front, rear
    if front == rear:
        return True
    return False

def enQueue(item):
    global front, rear
    if not isFull():
        rear = (rear+1)%(N+1)
        oven[rear] = item

def deQueue():
    global front, rear
    if not isEmpty():
        front = (front+1)%(N+1)
        return oven[front]

T=int(input())
for tc in range(T):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))
    oven = [0]*(N+1) # 길이: (N+1)
    front = 0
    rear = 0
    idx = 0

    while 1:
        if not isFull() and idx < len(input_list):
            enQueue([input_list[idx], idx])
            idx += 1
            continue
        else:
            pizza = deQueue()
            if pizza[0] // 2:
                enQueue([pizza[0]//2, pizza[1]])
            elif isEmpty():
                print(f'#{tc+1} {pizza[1]+1}')
                break

