#!/usr/bin/python3
"""
reddit_subscribers.py

A script to fetch the number of subscribers for a given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: Number of subscribers if successful, 0 if subreddit is invalid or error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0 (by /u/MyUsername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0


if __name__ == "__main__":
    subreddit = "learnpython"
    subscribers_count = number_of_subscribers(subreddit)
    print(f"The subreddit '{subreddit}' has {subscribers_count} subscribers.")
