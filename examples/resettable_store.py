import copy
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

store = fake_store.ResettableStore()
store.load_collection('pet', "nested_fake_store.yaml")

pets = store.mutable_collection(Pet, 'pet')
new_pet = copy.deepcopy(pets[0])
pets.append(new_pet)


store.reset_store()
restored_list_pets = store.mutable_collection(Pet, 'pet')

print(len(pets))
print(len(restored_list_pets))

