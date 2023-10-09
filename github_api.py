import sys

# Add the path to the requests library
sys.path.append('/path/to/requests')
import requests

def get_user_repositories_and_commits(username):
    try:
        # Get the user's repositories
        repo_url = f'https://api.github.com/users/{username}/repos'
        print(repo_url)
        response = requests.get(repo_url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        repos = response.json()

        repo_commits = []  # Initialize a list to store repo and commit count pairs

        # Iterate through the user's repositories
        for repo in repos:
            repo_name = repo['name']

            # Get the commits for each repository
            commit_url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
            commit_response = requests.get(commit_url)
            commit_response.raise_for_status()  # Raise an exception if the request was unsuccessful
            commits = commit_response.json()
            commit_count = len(commits)

            repo_commits.append((repo_name, commit_count))

        # Print the result
        for repo, commit_count in repo_commits:
            print(f"The repo {repo} has {commit_count} commits.")
        return repo_commits
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}")
        return None

# uName = input("Enter the username of a github you want to see info for: ")
# get_user_repositories_and_commits(uName)