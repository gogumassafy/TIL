test_num = int(input())

for tc in range(test_num):
    N = int(input())
    list_input = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N**2):



    print(f"#{tc+1}")
    for i in range(N):
        print(f"{' '.join(map(str, list_input[i]))}")