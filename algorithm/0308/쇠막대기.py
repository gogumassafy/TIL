raw_data = input()
cnt = 0
sol = 0
for i in range(len(raw_data)):
    if raw_data[i] == "(":
        cnt += 1
    else:
        cnt -= 1
        if raw_data[i - 1] == "(":
            sol += cnt
        else:
            sol += 1
print(sol)