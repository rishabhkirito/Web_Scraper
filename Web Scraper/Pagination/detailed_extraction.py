import requests
import csv
from csv import writer
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
headers = {
    "User-Agent": "Mozilla/5.0"
}

with open("book_desc.csv","w", newline = "", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title","product_description"])

    for page in range(1, 52):
        url = base_url.format(page)
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_ = "product_pod")


        for book in books:
            rating = book.p["class"][1]
            if rating == "Five":
                title = book.h3.a["title"]

                # Extract the relative URL from the anchor tag
                relative_url = book.h3.a["href"]
                book_url = "https://books.toscrape.com/catalogue/" + relative_url

                # Send a request to the book's page to get the product description
                book_response = requests.get(book_url, headers= headers)
                book_soup = BeautifulSoup(book_response.text, "html.parser")

                # Find the product description in the book's page
                product_description = book_soup.find("meta",attrs={"name": "description"})
                description = product_description["content"].strip() if product_description else "No description available"

                writer.writerow([title, description])
                print(f"Title: {title}")

            print(f"Page{page} completed")
        