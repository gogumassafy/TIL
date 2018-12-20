import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
req = requests.get(url).text
soup = BeautifulSoup(req, "html.parser")

for i in soup.select(".link"):
    name = i.select_one("a").text
    price = i.select_one(".idx").text
    print(name + "의 환율은 " + price + "입니다.")