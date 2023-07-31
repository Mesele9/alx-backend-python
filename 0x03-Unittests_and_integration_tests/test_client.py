#!/usr/bin/env python3
""" test_client.py """
from typing import Dict
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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
