"""This is a Python script that takes in a URL and an email address"""

import requests
import sys

def post_email(url, email):
    """The function used to enter the email address"""
    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <email>")
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        print(f"Your email is: {email}")
        post_email(url, email)
