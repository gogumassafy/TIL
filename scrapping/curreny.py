import requests
from bs4 import BeautifulSoup

# req = requests.get("http://www.cgv.co.kr/movies/").text
# soup = BeautifulSoup(req, "html.parser")
# kospi = soup.select_one("#contents > div.cols-rank > div.col-rank-search > div > ol")
# print(kospi.text)

# req = requests.get("https://www.naver.com/").text
# soup = BeautifulSoup(req, "html.parser")
# sheet = soup.select(".ah_item")
# for i in sheet:
#     each_sheet_text = i.select_one(".ah_k")
#     each_sheet_num = i.select_one(".ah_r")
#     print(each_sheet_num.text, each_sheet_text.text)


url = "http://www.naver.com"
req = requests.get(url).text
soup = BeautifulSoup(req, "html.parser")

for i in soup.select(".PM_CL_realtimeKeyword_list_base .ah_item"):
    rank = i.select_one(".ah_r").text
    name = i.select_one(".ah_k").text
    print(f"{rank}는 {name}입니다.")