"""This is a HTTP request code"""

import requests

def fetch_status():
    """This is a python script that fetches from the website"""
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    
    body = {
        "type": str(type(response.text)),
        "content": response.text
    }

    '''print("Body response:")
    print("    - type:", body["type"])
    print("    - content:", body["content"])'''

if __name__ == "__main__":
    fetch_status()
