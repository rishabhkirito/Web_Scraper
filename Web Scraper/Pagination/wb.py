import requests
from bs4 import BeautifulSoup
import re  # Import regex library

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url,headers=headers)

#print(response.status_code) #prints the status code of the response
#print(response.text[:500]) #prints the first 500 characters of the response

soup = BeautifulSoup(response.text,"html.parser")
books = soup.find_all("article" ,class_="product_pod")
print(f"Found {len(books)} Books")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.split()
    rating = book.p["class"][1]
    link = "https://books.toscrape.com/" +book.h3.a["href"]
    pages = book.find

    if rating == "Five":
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Availability: {availability}")
        print(f"Rating: {rating}")
        print(f"Link: {link}")
        print("-" * 60)  # Separator for readability

    else:
        continue  # Skip to the next iteration if the rating is not "Five"
       
