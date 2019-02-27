input_string = input()

total = 10
for i in range(1, len(input_string)):
    if input_string[i] == input_string[i-1]:
        total += 5
    else:
        total += 10

print(total)