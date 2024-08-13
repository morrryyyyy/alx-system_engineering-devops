#!/usr/bin/python3
"""This is an advanced task module."""
import requests
from collections import defaultdict


def count_words(subreddit, word_list, after=None, word_count=None):
    """Recursively count occurrences of keywords in the titles of hot posts."""
    if word_count is None:
        word_count = defaultdict(int)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'count_words:v1.0 (by /u/yourusername)'
    }
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        children = data.get('children', [])

        # Normalize word_list to lowercase
        word_list = [word.lower() for word in word_list]

        # Count occurrences of each keyword in the titles
        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                word_count[word] += title.split().count(word)

        # Handle pagination
        after = data.get('after', None)
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            # Sort the results by count and alphabetically
            sorted_word_count = sorted(
                word_count.items(),
                key=lambda item: (-item[1], item[0])
            )
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
    except requests.RequestException:
        return
