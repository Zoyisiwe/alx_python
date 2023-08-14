""" A Python script that takes in a letter and sends
 a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

def search_user(letter):
    """A POST request to the provided URL with the letter as a parameter"""
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        json_data = response.json()

        if json_data:
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    search_user(letter)
