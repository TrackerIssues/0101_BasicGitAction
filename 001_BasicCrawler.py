import requests
from bs4 import BeautifulSoup

sUrl ="https://ridibooks.com/category/bestsellers/2200"
oRes = requests.get(sUrl)
oRes.encoding = "utf-8"

soup = BeautifulSoup(oRes.text, "html.parser")


lstBook = soup.select("a.fig-rs5q24")

for no, book in enumerate(lstBook, 1) :
  print(no, book.text.strip())


