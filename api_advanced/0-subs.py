#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }
    response = requests.get(url)
    data = response.json()

    # Check if the subreddit exists and return the subscriber count
    if 'data' in data and 'subscribers' in data['data']:
        print("OK")
        return data['data']['subscribers']
    else:
        print("OK")
