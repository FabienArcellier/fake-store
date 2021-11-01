import copy
from typing import Type, TypeVar, List

from fake_store.load import load

KLASS = TypeVar('KLASS')

class Store:
    """

    >>> fake_store.bind_class(Pet.__name__, Pet)
    >>>
    >>> store = fake_store.Store()
    >>> store.load_collection('pet', "nested_fake_store.yaml")
    >>> pets = store.mutable_collection(Pet, 'pet')
    >>>

    """

    def __init__(self):
        self._store = {}

    def load_collection(self, key: str, path: str):
        self._store[key] = load(None, path)

    def mutable_collection(self, _klass: Type[KLASS], key) -> List[KLASS]:
        """
        return a mutable collection you can manipulate through different repository
        and keep consistency between them as a datastore would perform.

        """
        return self._store[key]


class ResettableStore:
    """

    >>> fake_store.bind_class(Pet.__name__, Pet)
    >>>
    >>> store = fake_store.ResettableStore()
    >>> store.load_collection('pet', "nested_fake_store.yaml")
    >>> pets = store.mutable_collection(Pet, 'pet')
    >>>
    >>> # the content of the store will be reset at the state of original dataset
    >>> store.reset_store()
    >>>
    """

    def __init__(self):
        self._original_store = {}
        self._store = {}

    def load_collection(self, key: str, path: str):
        content = load(None, path)
        self._store[key] = content
        self._original_store[key] = copy.deepcopy(content)

    def mutable_collection(self, _klass: Type[KLASS], key) -> List[KLASS]:
        """
        return a mutable collection you can manipulate through different repository
        and keep consistency between them as a datastore would perform.

        """
        return self._store[key]

    def reset_store(self):
        """
        reset the content of the store with the datasets loaded through load_collection.

        It may be useful to reset store content between automatic test without reloading data
        from disk.

        :return:
        """
        self._store = copy.deepcopy(self._original_store)
