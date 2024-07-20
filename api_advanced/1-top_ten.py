#!/usr/bin/python3
"""This script queries the Reddit API to fetch."""

import sys
import requests

def top_ten(subreddit):
    """Fetches and prints the titles of the first 10 hot posts for given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    params = {
        "limit":"10"
    }
    
    response = requests.get(url, headers=headers, params=params)
     data = response.json()
    
    for i, post in enumerate(data['data']['children'][:10], start=1):
        print(f"{i}. {post['data']['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reddit_api_query.py <subreddit>")
        sys.exit(1)
    
    subreddit = sys.argv[1]
    top_ten(subreddit)
