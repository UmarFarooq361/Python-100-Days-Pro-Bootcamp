import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
responce = requests.get(URL)
website_data = responce.text
soup = BeautifulSoup(website_data, "html.parser")
moviesTitle = soup.find_all(name="h3", class_="title")

top_100_movies = [items.getText() for items in moviesTitle] # list comprehension

# for head in moviesTitle:
#     title = head.getText()
#     top_100_movies.append(title)

# top_100_movies.reverse() # one way to reverse the list
# print(top_100_movies)

movies = top_100_movies[::-1]  #using slicing used to reverse the list

with open("top_movies.txt", "w") as file:
    for name in movies:
        file.write(f"{name}\n")

