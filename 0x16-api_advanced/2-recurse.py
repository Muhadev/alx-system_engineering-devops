#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The ID of the last post in the
        previous page (used for pagination).

    Returns:
        list: A list containing the titles of all hot articles
        for the subreddit, or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    """
    Custom User-Agent to prevent 429 Too Many Requests error
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        """
        Extract titles from current page and add to hot_list
        """
        for post in posts:
            hot_list.append(post['data']['title'])
        """
        If there are more pages, recursively call
        the function with the 'after' parameter
        """
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None
    elif response.status_code == 404:
        return None
    else:
        print("Error: Could not retrieve data from the Reddit API.")
        return None
