def left_up(present):
    return [present[0] - 1, present[1] - 1]


def right_up(present):
    return [present[0] - 1, present[1] + 1]


def left_down(present):
    return [present[0] + 1, present[1] - 1]


def right_down(present):
    return [present[0] + 1, present[1] + 1]


def tour(num_move, N):
    tour_list = []

    for i in range(1, num_move):
        tour_list.append([i, num_move - i])

    for T_list in tour_list:
        for i in range(N - num_move):
            for j in range(T_list[0], N - T_list[1]):
                check = False
                present = [i, j]
                visited = [cafe[present[0]][present[1]]]

                for _ in range(T_list[0]):
                    present = left_down(present)
                    visited.append(cafe[present[0]][present[1]])

                for _ in range(T_list[1]):
                    present = right_down(present)
                    visited.append(cafe[present[0]][present[1]])

                for _ in range(T_list[0]):
                    present = right_up(present)
                    visited.append(cafe[present[0]][present[1]])

                for _ in range(T_list[1] - 1):
                    present = left_up(present)
                    visited.append(cafe[present[0]][present[1]])

                hash_table = {}
                for k in visited:
                    if k in hash_table:
                        check = True

                    else:
                        hash_table[k] = 0
                #               print(visited)

                if not check:
                    return check, visited
    #               print(visited)

    return check, []


T = 1
# T = int(input())

for t in range(T):
    N = 4
    # N = int(input())


    cafe_input = ['9 8 9 8',
'4 6 9 4',
'8 7 7 8',
'4 5 3 5']
    cafe = []

    for i in range(N):
        cafe.append(list(map(int, cafe_input[i].split())))

    # cafe = []
    # for _ in range(N):
    #     cafe.append(list(map(int, input().split())))

    for i in reversed(range(2, N)):
        print(i)
        check, visited = tour(i, N)
        # print(check)
        if not check:
            break

    if check:
        point = -1
    else:
        point = len(visited)

    print('#%s %s' % (t + 1, point))