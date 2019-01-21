arr = [[0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11]]

#행 우선 탐색
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j])

#열 우선 탐색
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j])

#지그재그
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j + (len(arr[0])-1-2*j)*(i%2)])