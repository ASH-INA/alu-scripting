#!/usr/bin/python3
"""Module to fetch and print titles of the first 10 hot posts from a subreddit using the Reddit API."""

import requests

def top_ten(subreddit):
    """Fetches and prints the titles of the first 10 hot posts from the specified subreddit."""
    try:
        # Reddit API endpoint URL for fetching hot posts
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        
        # Set custom User-Agent header as Reddit API requires it
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Extract the JSON data from the response
            data = response.json()
            
            # Extract and print titles of the first 10 hot posts
            print(f"Top 10 hot posts in r/{subreddit}:")
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # If request was not successful, print None
            print(f"Error: Unable to fetch posts from r/{subreddit}. Status code: {response.status_code}")
            print("None")
    
    except requests.RequestException as e:
        # Handle any exception that occurred during the request
        print(f"Error: {e}")
        print("None")

if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    top_ten(subreddit)
