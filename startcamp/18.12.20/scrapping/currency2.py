import requests
from bs4 import BeautifulSoup

url = "https://m.stock.naver.com/marketindex/index.nhn"
req = requests.get(url).text
soup = BeautifulSoup(req, "html.parser")

ul = soup.select(".lst_wrp .item_lst li a")

for i in ul:
    item = i.select_one(".stock_item").text
    price = i.select_one(".stock_price").text
    print(item + "의 환율은 " + price + "입니다.")