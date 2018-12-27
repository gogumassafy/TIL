from bs4 import BeautifulSoup
import requests
import random

numbers = []
numbers = sorted(random.sample(range(800, 838), 8))
for i in numbers:
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    select_nums = soup.select(".nums")
    print(str(i) + "의 당첨번호")
    for j in select_nums:
        win_num = j.select(".win span")
        win_num_bonus = j.select_one(".bonus .ball_645").text
        for k in win_num:
            print(k.text, end=" ")
        print("+ "+ win_num_bonus)
        print()



#정리하는 버전
numbers = []
numbers = sorted(random.sample(range(800, 838), 8))
get_info(numbers)
print(str(i) + "의 당첨번호")
for j in select_nums:
    win_num = j.select(".win span")
    win_num_bonus = j.select_one(".bonus .ball_645").text
    for k in win_num:
        print(k.text + " ", end="")
    print("+ "+ win_num_bonus)
    print("")

def get_info(numbers):
    for i in numbers:
        url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)
        req = requests.get(url).text
        soup = BeautifulSoup(req, "html.parser")
        select_nums = soup.select(".nums")
    return 
def print_result():
