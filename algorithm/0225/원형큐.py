# C 스타일을 섞어서 쓴거.

SIZE = 4
Q = [0] * SIZE
front, rear = 0, 0

def isFull():
    global front, rear
    if (rear+1) % len(Q) == front:
        return True
    return False

def isEmpty():
    global front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(item):
    global front, rear
    if not isFull():
        rear = (rear + 1) % len(Q)
        Q[rear] = item

def deQueue():
    global front, rear
    if not isEmpty():
        front = (front + 1) % len(Q)
        return Q[front]

def Qpeek():
    global front, rear
    if not isEmpty():
        return Q[front+1]
    return
print(isEmpty())
enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
print(Q)
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(1)
enQueue(2)
enQueue(3)
print(isFull())
print(deQueue())
print(deQueue())
print(deQueue())
print(Q)