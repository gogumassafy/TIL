# 음수일떄 생각하기.
def itoa(number):
    input_list = []
    for i in range(len(number)):
        input_list[i] = chr((number % 10) + ord('0'))
        number //= 10
    input_list = input_list[::-1]
    print("".join(input_list))