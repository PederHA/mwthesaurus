import asyncio

import pytest

from mwthesaurus import MWClient


KEY = "YOUR-KEY-HERE"


@pytest.fixture(scope="session")
def client():
    return MWClient(key=KEY)


@pytest.fixture(scope="session")
def sync_result(client):
    return client.get("fat") # "fat" has multiple definitions
                             # thus we can test more cases


@pytest.fixture(scope="session")
def async_result(client):
    return asyncio.run(client.aget("fat"))
