import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
headers = {"User-Agent": "Mozilla/5.0"}

for page_num in range(1,51):
    url = base_url.format(page_num)
    response = requests.get(url,headers= headers)
    soup = BeautifulSoup(response.text,"html.parser")

    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        rating = book.p["class"][1]
        price = book.find("p", class_="price_color").text

        if rating == "Five":
            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Rating: {rating}")
            print("-" * 60)
        else:
            continue

    print(f"Page {page_num} processed.")