"""
A class dedicated to execute unit test with the library.
"""
from fake_store_tests.fixtures.store import Store


class Pet():

    def __init__(self, name: str, status: str, store: Store = None):
        self.name = name
        self.status = status
        self.store = store
