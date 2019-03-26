import queue

N = int(input())
raw = list(map(int, input().split()))
sum_cost = 0
q = queue.PriorityQueue()
if N == 1:
    sum_cost = raw[0]
else:
    raw.sort()
    for i in raw:
        q.put(i)
    a = q.get()
    while not q.empty():
        b = q.get()
        sum_cost += a + b
        q.put(a+b)
        a = q.get()
print(sum_cost)
