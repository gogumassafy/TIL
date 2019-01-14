
def is_babygin():
    data = [1, 3, 5, 7, 9, 9]
    for i1 in range(6):
        for i2 in range(6):
            if i1 != i2:
                for i3 in range(6):
                    if i1 != i3 and i2 != i3:
                        for i4 in range(6):
                            if i1 != i4 and i2 != i4 and i3 != i4:
                                for i5 in range(6):
                                    if i1 != i5 and i2 != i5 and i3 != i5 and i4 != i5:
                                        for i6 in range(6):
                                            if i1 != i6 and i2 != i6 and i3 != i6 and i4 != i6 and i5 != i6:
                                                chk = 0
                                                if data[i1] == data[i2] and data[i2] == data[i3]:
                                                    chk += 1
                                                if data[i4] == data[i5] and data[i5] == data[i6]:
                                                    chk += 1
                                                if data[i1] + 1 == data[i2] and data[i2] + 1 == data[i3]:
                                                    chk += 1
                                                if data[i4] + 1 == data[i5] and data[i5] + 1 == data[i6]:
                                                    chk += 1
                                                if chk == 2:
                                                    # print("Baby gin")
                                                    return "Baby gin"
    else:
        # print("Not baby gin")
        return "Not baby gin"
print(is_babygin())