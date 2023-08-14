"""A Python script that takes your GitHub credentials
 (username and password) and uses the GitHub API to display your id"""

import requests
import sys

def get_user_id(username, token):
    """User name and password for GitHub come in here"""
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"Basic {username}:{token}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print("Your GitHub user id is:", user_id)
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_user_id(username, token)
