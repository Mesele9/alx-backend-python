#!/usr/bin/env python3
""" test_client.py """
from typing import Dict
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized, parametirized_class
from client import GithubOrgClient
from requests import HTTPError
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ class to test GithubOrgCleint fucntion """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, orgName: str, resp: Dict, mock_json: MagicMock) -> None:
        """ Test the org method """
        mock_json.return_value = MagicMock(return_value=resp)
        org_client = GithubOrgClient(orgName)
        self.assertEqual(org_client.org(), resp)
        mock_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(orgName)
            )

    def test_public_repos_url(self) -> None:
        """ method to test public_repos_url property """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mocked_org:
            mocked_org.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                    GithubOrgClient("google")._public_repos_url,
                    "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_json: MagicMock) -> None:
        """ Test publi_repos method"""
        repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock
                          ) as mock_public_repos_url:
            mock_json.return_value = repos_payload
            org_client = GithubOrgClient("google")
            repos_list = org_client.public_repos()

            mock_json.assert_called_once_with(
                "https://api.github.com/users/google/repos"
            )

            self.assertEqual(repos_list, repos_payload)
