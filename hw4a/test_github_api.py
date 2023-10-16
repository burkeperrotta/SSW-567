import unittest
from unittest.mock import patch, MagicMock
from github_api import get_user_repositories_and_commits

class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')  # mock the get function
    def test_get_user_repositories_and_commits(self, mock_get):

        # make repository response
        mock_response_repos = MagicMock()
        mock_response_repos.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}, {'name': 'repo3'}, {'name': 'repo4'}, {'name': 'repo5'}, 
                                                 {'name': 'repo6'}, {'name': 'repo7'}, {'name': 'repo8'}, {'name': 'repo9'}]
        # make commit response
        mock_response_commits = MagicMock()
        mock_response_commits.json.return_value = [{'commit1'}, {'commit2'}]


        mock_get.side_effect = [mock_response_repos, mock_response_commits, mock_response_commits, mock_response_commits, mock_response_commits, 
                                mock_response_commits, mock_response_commits, mock_response_commits, mock_response_commits, mock_response_commits]

        username = "example_username"
        repo_commits = get_user_repositories_and_commits(username)
        

        # test theat the result isnt empty
        self.assertIsNotNone(repo_commits)

        # test that the result is the correct length
        self.assertEqual(len(repo_commits), 9)


        # test the different values in the result
        self.assertEqual(repo_commits[0], ('repo1', 2))
        self.assertEqual(repo_commits[1], ('repo2', 2))
        self.assertEqual(repo_commits[2], ('repo3', 2))
        self.assertEqual(repo_commits[3], ('repo4', 2))
        self.assertEqual(repo_commits[4], ('repo5', 2))
        self.assertEqual(repo_commits[5], ('repo6', 2))
        self.assertEqual(repo_commits[6], ('repo7', 2))
        self.assertEqual(repo_commits[7], ('repo8', 2))
        self.assertEqual(repo_commits[8], ('repo9', 2))

if __name__ == '__main__':
    unittest.main()


