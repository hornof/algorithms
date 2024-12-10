import unittest
from algorithms.arrays.delete_nth import delete_nth

class TestDeleteNth(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2), [1, 2, 3, 1, 2, 3])
        self.assertEqual(delete_nth([1, 1, 1, 1], 2), [1, 1])
        self.assertEqual(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 1), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(delete_nth([], 2), [])

    def test_single_element_list(self):
        self.assertEqual(delete_nth([1], 2), [1])
        self.assertEqual(delete_nth([1], 0), [])

    def test_all_elements_same(self):
        self.assertEqual(delete_nth([1, 1, 1, 1], 1), [1])
        self.assertEqual(delete_nth([1, 1, 1, 1], 3), [1, 1, 1])

    def test_no_elements_exceeding_n(self):
        self.assertEqual(delete_nth([1, 2, 3, 4, 5], 2), [1, 2, 3, 4, 5])
        self.assertEqual(delete_nth([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()