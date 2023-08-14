"""A python script that displays the body of the repsonse using URL"""

import requests
import sys

def fetch_and_display(url):
    """uses URL to display the body of the response using URL, and printing the error code"""
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display(url)
