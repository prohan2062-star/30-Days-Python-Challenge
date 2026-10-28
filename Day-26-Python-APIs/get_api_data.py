import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("Post ID:", data["id"])
    print("Title:", data["title"])
    print("Body:", data["body"])

except requests.RequestException as error:
    print("API request failed:", error)
except (ValueError, KeyError) as error:
    print("Data processing error:", error)
