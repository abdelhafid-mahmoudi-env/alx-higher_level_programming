#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of a given repository by a specified user on GitHub.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.RequestException as e:
        print(f"Error: {e}")
