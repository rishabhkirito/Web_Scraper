import csv
import requests
from bs4 import BeautifulSoup
import re  # Import regex library

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
headers = {
    "User-Agent": "Mozilla/5.0"
}

with open("book_ratings.csv", "w", newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "price", "availability", "rating", "lint"])

    for page in range(1, 52):
        url = base_url.format(page)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_ = "product_pod")

        for book in books:
            rating = book.p["class"][1]
            if rating == "Five":
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").text
                availability = book.find("p", class_="instock availability").text.split()
                link = "https://books.toscrape.com/" + book.h3.a["href"]

                writer.writerow([title, price, availability, rating, link])
        print(f"Page {page} completed")    
