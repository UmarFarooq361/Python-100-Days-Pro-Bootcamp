from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
yc_website_data = response.text
soup = BeautifulSoup(yc_website_data, "html.parser")

articles = (soup.find_all(name="span", class_="titleline"))
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)

    link = article.select_one(selector="a")
    article_links.append(link.get("href"))

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)



