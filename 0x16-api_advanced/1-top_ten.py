#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def top_ten(subreddit):
    """Function to return the top ten posts of a subreddit"""
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()['data']

    if response.status_code == 200 and 'children' in data:
        posts = data['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
