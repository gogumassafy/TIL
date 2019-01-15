import sys
sys.stdin = open("sample_input_card.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    case_input = input() #숫자를 문자로 받는다. 이유: 문자는 sequence 객체이기 때문에 순서를 이용할 수 있다.
    max_count = -float("inf")
    index_num = 0
    count_num = [0] * 10 # 0으로 초기화 된 배열 10개를 만든다. 어차피 숫자는 0~9밖에 존재하지 않으니까.

    for i in case_input:
        count_num[int(i)] += 1 # 개별 숫자들이 갯수를 세준다.

    for i in range(10): # 현재 카운트 횟수가 최대 카운트 횟수 보다 클 경우 바꿈.
        if count_num[i] > max_count:
            max_count = count_num[i]
            index_num = i
        elif count_num[i] == max_count and i > index_num: # 카운트 횟수가 현재 최대 카운트 같고 해당 숫자가 현재 최대 카운트 수보다 클 경우 바꿈.
            max_count = count_num[i]
            index_num = i

    print(f"#{tc+1} {index_num} {max_count}")

