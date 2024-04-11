#!/usr/bin/python3
"""
Queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    """
    Custom User-Agent to prevent 429 Too Many Requests error
    """
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
