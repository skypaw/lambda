import os

from typing import Protocol

import requests


class ClientProtocol(Protocol):
    def get(self, url: str, params: dict) -> requests.Response:
        pass


class Client(ClientProtocol):
    def __init__(self):
        self.session = requests.session()
        self.headers = {"Accept": "application/vnd.github+json",
                        "Authorization": f"Bearer {os.getenv('QUEUE')}",
                        "X-GitHub-Api-Version": "2022-11-28"}

    def get(self, url, params):
        response = self.session.get(url=url, params=params, headers=self.headers)
        return response.text
