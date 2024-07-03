import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json().get("data")
        return data.get("subscribers")  # Return number of subscribers
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return 0  # Subreddit not found
        else:
            print(f"HTTP error occurred: {http_err}")
            return None  # Handle other HTTP errors
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None  # Handle other exceptions
