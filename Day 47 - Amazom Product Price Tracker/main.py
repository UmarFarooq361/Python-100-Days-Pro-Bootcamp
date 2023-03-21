import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/dp/B01NBKTPTS/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B01NBKTPTS&pd_rd_w=XeB0I&"
header = {"Accept-language": "en-US,en;q=0.9",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/111.0.0.0 Safari/537.36"}
responce = requests.get(URL , headers= header)
website_data = responce.content
soup = BeautifulSoup(website_data, "lxml")
price = soup.find(name="span",class_="a-price-whole")
actaulPrice = price.getText()

print(soup.prettify())

# now send this to you by email using smtp module if price is less then certain amount and check it daily at 9am



