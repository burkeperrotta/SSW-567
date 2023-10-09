import requests
import json

def get_user_repositories_and_commits(username):
    try:
        # Get the user's repositories
        url = f'https://api.github.com/users/{username}/repos'
        rResponse = requests.get(url)
        # Raise an exception if the request was unsuccessful
        rResponse.raise_for_status()
        repos = rResponse.json()

        # make a list to store the repo and commit couples
        result = []

        # loop to iterate through all of the inputted user's repositories
        for repo in repos:
            name = repo['name']

            # use the same process to get all the commits for the relected repository
            commit_url = f'https://api.github.com/repos/{username}/{name}/commits'
            cResponse = requests.get(commit_url)
            # Raise an exception if the request was unsuccessful
            cResponse.raise_for_status()
            commits = cResponse.json()
            commit_num = len(commits)

            result.append((name, commit_num))

        return result

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        return None