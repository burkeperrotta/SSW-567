import unittest
from github_api import get_user_repositories_and_commits

class TestGitHubAPI(unittest.TestCase):

    def test_get_user_repositories_and_commits(self):
        username = "richkempinski"
        repo_commits = get_user_repositories_and_commits(username)

        #initial test to make sure function returns a result.
        self.assertIsNotNone(repo_commits)
        # test if the number of repos is correct
        self.assertEqual(len(repo_commits), 9)
        # test all of th eexample user's repos and commit numbers
        self.assertEqual(repo_commits[0], ('csp', 2))
        self.assertEqual(repo_commits[1], ('hellogitworld', 30))
        self.assertEqual(repo_commits[2], ('helloworld', 6))
        self.assertEqual(repo_commits[3], ('Mocks', 10))
        self.assertEqual(repo_commits[4], ('Project1', 2))
        self.assertEqual(repo_commits[5], ('richkempinski.github.io', 9))
        self.assertEqual(repo_commits[6], ('threads-of-life', 1))
        self.assertEqual(repo_commits[7], ('try_nbdev', 2))
        self.assertEqual(repo_commits[8], ('try_nbdev2', 5))


if __name__ == '__main__':
    unittest.main()