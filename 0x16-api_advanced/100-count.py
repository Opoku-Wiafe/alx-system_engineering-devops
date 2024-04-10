#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers"""

import requests
import re
from collections import Counter

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def count_words(subreddit, word_list, counts=None, after=None):
    """occurrences of words in the titles of hot posts from a subreddit."""
    if counts is None:
        counts = Counter()

    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()['data']
    titles = [post['data']['title'] for post in data['children']]

    for title in titles:
        words = re.findall(r'\b\w+\b', title.lower())
        for word in words:
            if word in word_list:
                counts[word] += 1

    if 'after' in data and data['after'] is not None:
        count_words(subreddit, word_list, counts, data['after'])
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f'{word}: {count}')


# count_words('python', ['python', 'java', 'javascript'])
count_words('programming', ['python', 'java', 'javascript'])
