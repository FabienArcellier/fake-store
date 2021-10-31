import os
import unittest

import fake_store
from fake_store_tests.fixtures import FIXTURE_DIR
from fake_store_tests.fixtures.pet import Pet
from fake_store_tests.fixtures.store import Store


class TestLoad(unittest.TestCase):

    def test_load_should_return_a_list_of_pets(self):
        # Assign
        pet_path = os.path.join(FIXTURE_DIR, "pets.yaml")
        fake_store.bind_class(Pet.__name__, Pet)


        # Acts
        list_of_pets = fake_store.load(Pet, pet_path)

        # Assert
        self.assertEqual(2, len(list_of_pets))
        self.assertIsInstance(list_of_pets[0], Pet)
        self.assertEqual("Ronny", list_of_pets[0].name)

    def test_load_should_return_a_list_of_pets_and_store_in_nested_definition(self):
        # Assign
        pet_path = os.path.join(FIXTURE_DIR, "pets_with_store.yaml")
        fake_store.bind_class(Pet.__name__, Pet)
        fake_store.bind_class(Store.__name__, Store)


        # Acts
        list_of_pets = fake_store.load(Pet, pet_path)

        # Assert
        self.assertEqual(2, len(list_of_pets))
        self.assertIsInstance(list_of_pets[0].store, Store)


if __name__ == '__main__':
    unittest.main()
