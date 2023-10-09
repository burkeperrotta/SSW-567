import unittest
from hw4a.github_api import get_user_repositories_and_commits

class TestGitHubAPI(unittest.TestCase):

    def test_get_user_repositories_and_commits(self):
        username = "richkempinski"
        repo_commits = get_user_repositories_and_commits(username)

        self.assertIsNotNone(repo_commits)  # Ensure the function returns a result

        # Add specific test cases here
        # For example:
        # self.assertEqual(len(repo_commits), expected_number_of_repositories)
        # self.assertEqual(repo_commits[0], ('RepoName', expected_commit_count))

if __name__ == '__main__':
    unittest.main()