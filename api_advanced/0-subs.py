#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0 (by /u/MyUsername)'}

    try:
        """Try fetching"""
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            """If ok return subscribers"""
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            """Else return 0"""
            return 0
    except requests.exceptions.RequestException as e:
        """Catch exceptions"""
        print(f"Error fetching data: {e}")
        return 0
