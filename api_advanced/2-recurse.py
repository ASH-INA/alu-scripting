#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, params={'after': hot_list.get('after', '')}, allow_redirects=False)

    if response.status_code == 404:
        return None

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            hot_list.append(post['data']['title'])

        # Recursive call to get next page
        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list

    except Exception:
        return None
