original_list = [[0 for _ in range(5)] for _ in range(5)]

original_list[0] = [9, 20, 2, 18, 11]
original_list[1] = [19, 1, 25, 3, 21]
original_list[2] = [8, 24, 10, 17, 7]
original_list[3] = [15, 4, 16, 5, 6]
original_list[4] = [12, 13, 22, 23, 14]

row, column =len(original_list), len(original_list[0])

# row, column
direction = [0, 1]
location = [0, 0]

for _ in range(25):
    original_list[location[0]][location[1]] = 1

    if location[0] + direction[0] < row and location[0] + direction[0] >= 0:
        location[0] += direction[0]
    elif location[0] + direction[0] >= row:
        direction[1] = -1
        direction[0] = 0
        column -= 1
        location[1] += direction[1]
    else:
        direction[1] = 1
        direction[0] = 0
        column -= 1
        location[1] += direction[1]

    if location[1] + direction[1] < column and location[1] + direction[1] >= 0:
        location[1] += direction[1]
    elif location[1] + direction[1] >= column:
        direction[0] = 1
        direction[1] = 0
        row -= 1
        location[0] += direction[0]
    else:
        direction[0] = -1
        direction[1] = 0
        row -= 1
        location[0] += direction[0]

