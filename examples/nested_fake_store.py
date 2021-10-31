from dataclasses import dataclass
from typing import Optional

import fake_store


@dataclass
class Store:
    city: str


@dataclass
class Pet:
    name: str
    status: str
    store: Optional[Store] = None


fake_store.bind_class(Pet.__name__, Pet)
fake_store.bind_class(Store.__name__, Store)

pets = fake_store.load(Pet, "nested_fake_store.yaml")
[print(pet) for pet in pets]


