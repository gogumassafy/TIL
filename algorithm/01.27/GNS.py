import sys
sys.stdin = open("GNS_input.text")

test = int(input())
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(test):
    input_number = input().split()
    input_list = input().split()
    num_count_list = [0] * 10
    for i in range(10):
        num_count_list[i] = input_list.count(num_list[i])

    print(input_number[0])
    for i in range(len(num_count_list)):
        print(f"{num_list[i]} " * num_count_list[i], end="")
    print()