# f = open("test.txt", "w", encoding = "utf-8")
# for i in range(1,6):
#     f.write(f"{i}번째 줄입니다. \t")
# f.close()

with open("new.txt", "r", encoding = "utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)