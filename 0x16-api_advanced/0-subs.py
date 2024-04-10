#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """Function to return the number of subscribers of a subreddit"""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json()['data']
    if response.status_code == 200 and 'subscribers' in data:
        return data['subscribers']
    else:
        return 0
