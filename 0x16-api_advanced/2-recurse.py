#!/usr/bin/python3
"""This is the 2-recurse module."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively get titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'recurse:v1.0 (by /u/yourusername)'
    }
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            for child in children:
                hot_list.append(child['data']['title'])
            # Get the next page's "after" parameter
            after = data.get('after', None)
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
