def bubbleSort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


data = [55, 7, 78, 12, 42]
bubbleSort(data)
print(data)

def bubbleSortReverse(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


data = [55, 7, 78, 12, 42]
bubbleSortReverse(data)
print(data)