#!/usr/bin/python3
''' This is the 0-subs.py module.'''
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom'}

    try:
        print(f"Requesting URL: {url}")  # Debug: Print the URL
        response = requests.get(url, headers=headers, allow_redirects=False)

        print(f"Response Status Code: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Response Data: {data}")  # Debug: Print the JSON data
                return data['data'].get('subscribers', 0)
            except ValueError:
                # Handle JSON decoding error
                print("JSON decoding failed")  # Debug: JSON decoding error
                return 0
        else:
            return 0
    except requests.RequestException as e:
        # Log or print the exception for debugging
        print(f"Request failed: {e}")
        return 0
