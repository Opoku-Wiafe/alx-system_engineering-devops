#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers"""

import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def recurse(subreddit, hot_list=[], after=None):
    """Function to return the top ten posts of a subreddit"""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list += [post['data']['title'] for post in data['children']]

    if 'after' in data and data['after'] is not None:
        return recurse(subreddit, hot_list, data['after'])
    else:
        return hot_list
