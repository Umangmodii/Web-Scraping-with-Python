import requests
from bs4 import BeautifulSoup

url = "https://umangmodi.netlify.app/"

# Step 1 : Get the Data

content = requests.get(url)
htmlcontent = content.content
# print(htmlcontent)

# Step 2 : Parsed the Data

soup = BeautifulSoup(htmlcontent,"html.parser")
# print(soup.prettify())

# Step 3 : HTML with Tree Traversal
# title = soup.title
# print(type(title))

# Paragraph Find
# paragraph = soup.find_all('p')
# print(paragraph)

# Anchor Find
anchor = soup.find_all('a')
print(anchor)

for link in anchor:
    print(link.get("href"))