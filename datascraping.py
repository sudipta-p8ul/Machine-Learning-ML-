import requests
from bs4 import BeautifulSoup

# Step 1: Target URL
url = "https://www.bbc.com/sport"

# Step 2: Send HTTP request
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines
headlines = soup.select("h3.fc-item__title")

print("Latest Tech News from The Guardian:\n")
for h in headlines:
    print("-", h.get_text(strip=True))