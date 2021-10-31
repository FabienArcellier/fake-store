from dataclasses import dataclass
from typing import Optional, Tuple

import fake_store


@dataclass
class Store:
    city: str
    gps: Tuple[int, int]

    @classmethod
    def create_with_gps(cls, city: str):
        gps = (12, 12) if city == "New York" else (0, 0)

        return Store(city, gps)


@dataclass
class Pet:
    name: str
    status: str
    store: Optional[Store] = None


fake_store.bind_class(Pet.__name__, Pet)
fake_store.bind_class(Store.__name__, Store)

pets = fake_store.load(Pet, "factory_fake_store.yaml")
[print(pet) for pet in pets]


