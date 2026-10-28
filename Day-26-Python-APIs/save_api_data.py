import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    posts = response.json()

    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)

    print(f"Successfully saved {len(posts)} posts.")
    print("Data saved to posts.json")

except requests.RequestException as error:
    print("API request failed:", error)
except (ValueError, TypeError) as error:
    print("Data processing error:", error)
