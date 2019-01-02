import random
import requests
import json
from pprint import pprint

"""
random으로 로또번호 생성
api를 통해 우승 번호 가져옴
위 두 행위를 비교하여 나의 등수를 알려준다.

1. url 요청 보내서 정보 가져옴.
    1-1.json으로 받는다. (딕셔너리로 접근 가능)
2. api의 당첨번호와 보너스 번호를 저장한다.
3. 뽑은게 몇등인지 확인한다.
"""

"""
count_i_try = 0


while True:
    my_num = []
    my_num = random.sample(range(1, 46), 6)
    count_i_try += 1

    input_status = 1
    count_i_won = 0
    bool_bonus = 0
    win_nums = []

    # while input_status:
    #     what_time_do_you_want = input("원하는 회차를 입력하세요(숫자, 1~837): ")
    #     if int(what_time_do_you_want) > 1 and int(what_time_do_you_want) < 838:
    #         input_status = 0

    # url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(what_time_do_you_want)

    url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    req = requests.get(url)
    lotto = req.json()

    for i in range(1, 7):
        win_nums.append(lotto["drwtNo"+str(i)])

    for i in range(0,6):
        for j in win_nums:
            if j == my_num[i]:
                count_i_won += 1

    # if count_i_won < 3:
    #     print("꽝")
    # elif count_i_won == 3:
    #     print("5등 입니다.")
    # elif count_i_won == 4:
    #     print("4등 입니다")
    if count_i_won == 5:
        for i in range(0,6):
            if lotto["bnusNo"] == my_num[i]:
                bool_bonus = 1
                break
        if bool_bonus:
            print("2등입니다.")
            print(str(count_i_try) + "번만큼 시도하여 2등이 되었습니다.")
        else:
            print("3등입니다.")
            print(str(count_i_try) + "번만큼 시도하여 3등이 되었습니다.")
    elif count_i_won == 6:
        print("1등 입니다.")
        break
print(str(count_i_try) + "번만큼 시도하여 1등이 되었습니다.")
"""

"""
세트에 관한 이론
1. 세트는 중복, 순서가 없다
2. 세트를 생성하기 위해서는  a = {}가 아니라 a = set()으로 생성해야 한다. 전자는 딕셔너리다.

차집합, 교집합, 합집합 등 실시

set1 = set([1, 2, 3, 4, 5, 6, 7,])
set2 = set([5, 6, ,7, 8, 9, 10, 11])
교집합: set1 & set2, set1.intersection(set2)
=> {5, 6, 7}

합집합: set1 | set2, set.union(set2)

차집합: set2 - set1
"""


#세트를 이용한 풀이.
win_nums = set()
count_i_try = 0

# input_status = 1
# while input_status:
#     what_time_do_you_want = input("원하는 회차를 입력하세요(숫자, 1~837): ")
#     if int(what_time_do_you_want) > 1 and int(what_time_do_you_want) < 838:
#         input_status = 0

# url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(what_time_do_you_want)

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
req = requests.get(url)
lotto = req.json()

for i in range(1, 7):
    win_nums.add(lotto["drwtNo" + str(i)])

while True:
    count_i_try += 1
    my_num = set(random.sample(range(1,47), 6))
    checklen = len(my_num - win_nums)

    if checklen == 0:
        break
    elif checklen == 1:
        if lotto["bnusNo"] in my_num:
            print(str(format(count_i_try, ",")) + "번만큼 시도하여 2등이 되었습니다.")
        else:
            print(str(format(count_i_try, ",")) + "번만큼 시도하여 3등이 되었습니다.")
    # elif checklen == 2:
    #     print(str(count_i_try) + "번만큼 시도하여 4등이 되었습니다.")

print(str(format(count_i_try, ",")) + "번만큼 시도하여 1등이 되었습니다.")