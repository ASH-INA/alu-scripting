#!/usr/bin/python3

"""
Reddit API Query

This script queries the Reddit API to fetch and print the titles of the first
10 hot posts for a given subreddit.

Usage:
    $ python3 reddit_api_query.py

Requirements:
    - Python 3.4.3 or higher
    - Requests module (install with `pip install requests`)
    - Proper internet connection

"""

import sys
import requests
import logging

def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch posts from.

    Prints:
        Prints the titles of the first 10 hot posts. If the subreddit is invalid,
        prints None.

    """
    # Reddit API endpoint URL for getting hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set custom User-Agent header to prevent 429 (rate limit exceeded) responses
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Extract JSON data from the response
        data = response.json()
        
        # Iterate over the first 10 posts and print their titles
        for i, post in enumerate(data['data']['children'][:10], start=1):
            print(f"{i}. {post['data']['title']}")
    
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        print(None)
    
    except ValueError as val_err:
        logging.error(f"Value error occurred: {val_err}")
        print(None)
    
    except Exception as err:
        logging.error(f"An error occurred: {err}")
        print(None)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reddit_api_query.py <subreddit>")
        sys.exit(1)
    
    subreddit = sys.argv[1]
    top_ten(subreddit)

