import requests

def get_user_repositories_and_commits(username):
        # Get the user's repositories
        repo_url = f'https://api.github.com/users/{username}/repos'
        print(repo_url)
        response = requests.get(repo_url)
        repos = response.json()

        repo_commits = []  # Initialize a list to store repo and commit count pairs

        # Iterate through the user's repositories
        for repo in repos:
            repo_name = repo['name']

            # Get the commits for each repository
            commit_url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
            commit_response = requests.get(commit_url)
            commits = commit_response.json()
            commit_count = len(commits)

            repo_commits.append((repo_name, commit_count))

        return repo_commits


# uName = input("Enter the username of a github you want to see info for: ")
# get_user_repositories_and_commits(uName)
