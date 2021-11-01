import copy
import os
import unittest

import fake_store
from fake_store_tests.fixtures import FIXTURE_DIR
from fake_store_tests.fixtures.pet import Pet


class TestStore(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_should_return_a_the_same_reference(self):
        # Assign
        pet_path = os.path.join(FIXTURE_DIR, "pets.yaml")
        fake_store.bind_class(Pet.__name__, Pet)

        store = fake_store.Store()
        store.load_collection('pet', pet_path)

        list_of_pets = store.mutable_collection(Pet, 'pet')
        new_pet = copy.deepcopy(list_of_pets[0])
        list_of_pets.append(new_pet)

        # Acts
        same_list_of_pets = store.mutable_collection(Pet, 'pet')

        # Assert
        self.assertIs(list_of_pets, same_list_of_pets)

    def test_reset_store_should_restore_the_origin_record(self):
        # Assign
        pet_path = os.path.join(FIXTURE_DIR, "pets.yaml")
        fake_store.bind_class(Pet.__name__, Pet)

        store = fake_store.ResettableStore()
        store.load_collection('pet', pet_path)

        list_of_pets = store.mutable_collection(Pet, 'pet')
        new_pet = copy.deepcopy(list_of_pets[0])
        list_of_pets.append(new_pet)

        store.reset_store()

        # Acts
        different_list_of_pets = store.mutable_collection(Pet, 'pet')

        # Assert
        self.assertIsNot(list_of_pets, different_list_of_pets)
        self.assertEqual(3, len(list_of_pets))
        self.assertEqual(2, len(different_list_of_pets))



if __name__ == '__main__':
    unittest.main()
