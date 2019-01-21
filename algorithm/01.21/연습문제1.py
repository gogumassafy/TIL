d_row = [0, 0, -1, 1]
d_col = [-1, 1, 0, 0]

arr = [[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]
sum = 0

for row in range(len(arr)):
    for col in range(len(arr[0])):
        for i in range(4):
            test_row = row + d_row[i]
            test_col = col + d_col[i]
            if test_row in range(5) and test_col in range(5):
                sum += abs(arr[test_row][test_col] - arr[row][col])
print(sum)