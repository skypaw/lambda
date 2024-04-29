from github import Client, ClientProtocol


class Queue:
    def __init__(self, api_client: ClientProtocol):
        self.client = api_client

    def list_items(self):
        items = self.client.get(url='https://api.github.com/repos/skypaw/lambda-actions/actions/workflows/queue.yml/runs',
                                params={})
        print(items)


def exceeds_threshold():
    pass


def queue_empty():
    pass


if __name__ == "__main__":
    client = Client()
    Queue(client).list_items()
