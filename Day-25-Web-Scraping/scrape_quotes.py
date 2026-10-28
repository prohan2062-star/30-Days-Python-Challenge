import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for item in quotes:
        text = item.find("span", class_="text").get_text(strip=True)
        author = item.find("small", class_="author").get_text(strip=True)

        print("Quote:", text)
        print("Author:", author)
        print("-" * 50)

except requests.RequestException as error:
    print("Request error:", error)
