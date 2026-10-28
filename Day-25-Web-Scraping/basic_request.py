import requests

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Website fetched successfully!")
        print(response.text[:500])
    else:
        print("Request failed.")

except requests.RequestException as error:
    print("Error:", error)
