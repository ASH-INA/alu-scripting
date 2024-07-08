#!/usr/bin/python3
"""Module for task 0"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)"
    headers = {'User-Agent': 'MyBot/0.1'}  # Replace with your desired user-agent

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Check if the subreddit exists and return the subscriber count
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0  # Subreddit not found or invalid
        
    except requests.RequestException as e:
        print(f"Error fetching subreddit data: {e}")
        return 0

