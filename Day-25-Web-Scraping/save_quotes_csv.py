import csv
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    with open(
        "quotes.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])

        for item in quotes:
            quote = item.find("span", class_="text").get_text(strip=True)
            author = item.find("small", class_="author").get_text(strip=True)

            tags = [
                tag.get_text(strip=True)
                for tag in item.find_all("a", class_="tag")
            ]

            writer.writerow([quote, author, ", ".join(tags)])

    print(f"Saved {len(quotes)} quotes to quotes.csv")

except requests.RequestException as error:
    print("Request error:", error)
