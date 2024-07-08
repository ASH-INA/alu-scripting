#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}
    
    try:
        """Module for task 0"""
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            """Module for task 0"""
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            """Module for task 0"""
            return 0
    
    except requests.RequestException as e:
        """Module for task 0"""
        print(f"Error fetching data from Reddit API: {e}")
        return 0
