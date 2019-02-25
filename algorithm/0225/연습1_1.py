# C 스타일을 섞어서 쓴거.

SIZE = 100
Q = [0] * SIZE
front, rear = -1, -1
def isFull():
    global front, rear
    if rear+1 == SIZE:
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
        rear += 1
        Q[rear] = item

def deQueue():
    global front, rear
    if not isEmpty():
        front += 1
        return Q[front]

def Qpeek():
    global front, rear
    if not isEmpty():
        return Q[front+1]
    return

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())