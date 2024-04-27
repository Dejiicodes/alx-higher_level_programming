#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
from requests import get
import sys


if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        r = get(url)
        r.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        json_o = r.json()
        for i in range(min(10, len(json_o))):
            commit = json_o[i].get('commit')
            author = commit.get('author').get('name')
            sha = json_o[i].get('sha')
            print("{}: {}".format(sha, author))
    except IndexError:
        print("Usage: ./100-github_commits.py <repo> <owner>")
        sys.exit(1)
    except KeyError as e:
        print("KeyError: {}".format(e))
        sys.exit(1)
    except Exception as e:
        print("An error occurred: {}".format(e))
        sys.exit(1)
