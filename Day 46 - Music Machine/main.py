import requests
from bs4 import BeautifulSoup

# your_age = (input("Enter your age in YYYY-MM-DD : "))
your_age = "2000-08-12"
URL = f"https://www.billboard.com/charts/hot-100/{your_age}"
responce = requests.get(URL)
website_data = responce.text
soup = BeautifulSoup(website_data, "html.parser")

songTitle = soup.select("li #title-of-a-story")

top_100_songs = [items.text.strip() for items in songTitle]  #list comprehension

print(top_100_songs)
# with open("top_movies.txt", "w") as file:
#     for name in movies:
#         file.write(f"{name}\n")


