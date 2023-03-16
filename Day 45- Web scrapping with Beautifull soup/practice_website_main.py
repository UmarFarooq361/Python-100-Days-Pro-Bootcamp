from bs4 import BeautifulSoup


with open("website.html","rb") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string) # print text in title tag
# print(soup.a) # print first anchor tag
# print(soup.prettify()) # print all content pretty

all_tags = soup.find_all(name="a")
# print(all_tags)
for tag in all_tags:
    # print(tag.getText()) #will print text in anchor tags
    print(tag.get("href"))
    # will just get the href of all anchor tags

heading = soup.find(name="h1", id="name")
#this will search id for more spacific content
print(heading)

url = soup.select_one(selector="p a")
#narrow downing to particular link
print(url)
all_headings = soup.select(".heading")
#using class selector
print(all_headings)