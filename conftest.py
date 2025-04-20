import pytest
from .main import BooksCollector


@pytest.fixture(autouse=True)
def collector(self):
    collector = BooksCollector()
    return collector
