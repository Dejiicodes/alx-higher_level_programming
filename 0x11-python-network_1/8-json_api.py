#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except IndexError:
        pass

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        r.raise_for_status()  # Raise an exception for 4xx/5xx status codes
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

    try:
        json_o = r.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except ValueError:
        print("Not a valid JSON")
