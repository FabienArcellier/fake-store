import unittest

import fake_store
from fake_store_tests.fixtures.pet import Pet


class TestBinding(unittest.TestCase):

    def test_bind_class_should_work_with_class(self):
        # Assign
        # Acts
        fake_store.bind_class(Pet.__name__, Pet)

        # Assert
        binded_class = fake_store.binding.binded_class(Pet.__name__)
        self.assertIs(binded_class, Pet)


if __name__ == '__main__':
    unittest.main()
