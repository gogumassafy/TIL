
input_list = [[4,4,3,2,1],
              [2,2,1,6,5],
              [3,5,4,6,7],
              [4,2,5,9,7],
              [8,1,9,5,6]]

#가로 합
row_sum = 0
for i in range(4):
    if sum(input_list[i]) > sum(input_list[i+1]):
        row_sum = sum(input_list[i])
    else:
        row_sum = sum(input_list[i+1])

#세로 합
col_sum = 0
for i in range(5):
    each = 0
    for j in range(5):
        each += input_list[j][i]
    if each > col_sum:
        col_sum = each

#대각선 합
dia_sum1 = 0
dia_sum2 = 0
for i in range(5):
    dia_sum1 += input_list[i][i]
    dia_sum2 += input_list[i][4-i]

print(row_sum, col_sum, dia_sum2, dia_sum1)
print(f"#{max(row_sum, col_sum, dia_sum2, dia_sum1)}")