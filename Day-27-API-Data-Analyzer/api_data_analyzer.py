import csv
import json
import requests
from collections import Counter

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    """Fetch posts from the public testing API."""
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()

    posts = response.json()

    if not isinstance(posts, list):
        raise ValueError("Unexpected API response format.")

    return posts


def analyze_posts(posts):
    """Calculate summary statistics from API data."""
    user_counts = Counter(
        post["userId"]
        for post in posts
        if "userId" in post
    )

    return {
        "total_posts": len(posts),
        "unique_users": len(user_counts),
        "posts_per_user": dict(user_counts),
        "longest_title": max(
            (post.get("title", "") for post in posts),
            key=len,
            default=""
        )
    }


def save_csv(posts):
    """Save post data to a CSV file."""
    with open(
        "posts_report.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["userId", "id", "title", "body"]
        )
        writer.writeheader()

        for post in posts:
            writer.writerow({
                "userId": post.get("userId", ""),
                "id": post.get("id", ""),
                "title": post.get("title", ""),
                "body": post.get("body", "")
            })


def main():
    try:
        posts = fetch_posts()
        report = analyze_posts(posts)

        with open(
            "analysis_report.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(report, file, indent=4)

        save_csv(posts)

        print("=== API DATA ANALYZER ===")
        print("Total posts:", report["total_posts"])
        print("Unique users:", report["unique_users"])
        print("\nPosts per user:")

        for user_id, count in report["posts_per_user"].items():
            print(f"User {user_id}: {count} posts")

        print("\nLongest title:", report["longest_title"])
        print("\nReports saved successfully!")
        print("- posts_report.csv")
        print("- analysis_report.json")

    except requests.RequestException as error:
        print("API request failed:", error)
    except (ValueError, KeyError, TypeError) as error:
        print("Data processing failed:", error)


if __name__ == "__main__":
    main()
