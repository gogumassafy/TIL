# with open("test.txt", "w", encoding = "utf-8") as f:
#     for i in range(1,6):
#         f.write(f"{i}번째 줄입니다.\t")

f = open("test.txt", "w", encoding = "utf-8")
for i in range(1,6):
    f.write(f"{i}번째 줄입니다.\t")
f.close()