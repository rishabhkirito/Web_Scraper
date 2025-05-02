import requests
from bs4 import BeautifulSoup
import re  # Import regex library

# Step 1: Request the GitHub page
url = "https://github.com/trending"  # Scrape trending repos as an example
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract and filter GitHub repository links
repo_pattern = re.compile(r"^/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+$")  # Matches "/username/repo-name"
count = 0
max_links = 5  # Limit results

for link in soup.find_all("a", href=True):  # Find all <a> tags with href
    href = link["href"]
    if repo_pattern.match(href):  # Check if href matches the GitHub repo pattern
        full_url = "https://github.com" + href  # Convert relative URL to absolute
        print(full_url)
        count += 1
        if count >= max_links:  # Stop after 5 links
            break
