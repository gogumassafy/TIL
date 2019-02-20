def bubbleSort(data):
    for i in range(1, len(data)):
        for j in range(len(data)-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

def reversebubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)-(i+1)):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

data = [55, 7, 78, 12, 42]
bubbleSort(data)
print(data)
reversebubbleSort(data)
print(data)