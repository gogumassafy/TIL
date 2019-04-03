raw = [int(input()) for _ in range(10)]
mario = 0
for i in range(len(raw)):
    if abs(100 - (mario + raw[i])) <= abs(100 - mario):
        mario += raw[i]
    else:
        break
print(mario)
