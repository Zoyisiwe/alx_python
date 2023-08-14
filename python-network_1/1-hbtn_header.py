"""This is a python script that takes a URL as a input"""

import requests
import sys

def fetch_request_id(url):
    """A function that uses a URL as a input"""
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    if request_id is not None:
        print(request_id)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        fetch_request_id(url)
