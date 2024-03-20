import requests
from bs4 import BeautifulSoup

r = requests.get("https://umangmodi.netlify.app/")

print(r.url)

print(r.status_code)