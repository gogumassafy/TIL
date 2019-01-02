# from bs4 import BeautifulSoup
# import requests
# import random

# numbers = []
# numbers = sorted(random.sample(range(800, 838), 8))
# for i in numbers:
#     url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)
#     req = requests.get(url).text
#     soup = BeautifulSoup(req, "html.parser")
#     select_nums = soup.select(".nums")
#     print(str(i) + "의 당첨번호")
#     for j in select_nums:
#         win_num = j.select(".win span")
#         win_num_bonus = j.select_one(".bonus .ball_645").text
#         for k in win_num:
#             print(k.text, end=" ")
#         print("+ "+ win_num_bonus)
#         print()



# #정리하는 버전
# numbers = []
# numbers = sorted(random.sample(range(800, 838), 8))
# get_info(numbers)
# print(str(i) + "의 당첨번호")
# for j in select_nums:
#     win_num = j.select(".win span")
#     win_num_bonus = j.select_one(".bonus .ball_645").text
#     for k in win_num:
#         print(k.text + " ", end="")
#     print("+ "+ win_num_bonus)
#     print("")

# def get_info(numbers):
#     for i in numbers:
#         url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)
#         req = requests.get(url).text
#         soup = BeautifulSoup(req, "html.parser")
#         select_nums = soup.select(".nums")
#     return 

# def print_result():

import random, requests as req
from bs4 import BeautifulSoup

# 8회차 분량의 당첨번호 뽑아오기 (web crawling)
def main():
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
    numbers = sorted(random.sample(range(810,838), 8))
    for num in numbers:
        search = url + str(num)
        data = _get_data(search)
        _print(num, data)

def _get_data(url):
    res = req.get(url).text
    soup = BeautifulSoup(res, "html.parser")
    lucky = soup.select_one(".win_result")
    wins = lucky.select(".win .ball_645")
    bonus = lucky.select_one(".bonus .ball_645").text
    return wins, bonus

def _print(num, data):
    result = []
    for win in data[0]:
        result.append(win.text)
        print(result)
    print(f"{num}회차 당첨번호")
    for r in result:
        print(f"{r}", end=" ")
    print(f"+ {data[1]}")

if __name__ == "__main__":
    main()