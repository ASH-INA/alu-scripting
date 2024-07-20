#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code == 200:
        """Extract the JSON data from the response"""
        data = response.json()
        
        """Extract and print titles of the first 10 hot posts"""
        print(f"Top 10 hot posts in r/{subreddit}:")
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        """If request was not successful, print None"""
        print(f"Error: Unable to fetch posts from r/{subreddit}. Status code: {response.status_code}")
        print("None")

if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    top_ten(subreddit)
