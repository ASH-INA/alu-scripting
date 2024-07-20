#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json()
    for post in data['data']['children']:
            print(post['data']['title'])
