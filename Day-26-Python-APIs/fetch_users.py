import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    users = response.json()

    print("Total users:", len(users))
    print("\nUser Details:")

    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("-" * 30)

except requests.RequestException as error:
    print("Unable to fetch users:", error)
except (ValueError, KeyError, TypeError) as error:
    print("Data processing error:", error)
