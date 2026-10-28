import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a", href=True):
        text = link.get_text(strip=True)
        full_url = urljoin(url, link["href"])

        print(f"Text: {text or '[No text]'}")
        print(f"URL: {full_url}")
        print("-" * 40)

except requests.RequestException as error:
    print("Request error:", error)
