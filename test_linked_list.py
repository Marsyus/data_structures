import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_at_beginning(self):
        self.linked_list.insert_at_beginning(1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.linked_list.insert_at_beginning(2)
        self.assertEqual(self.linked_list.head.data, 2)

    def test_insert_at_end(self):
        self.linked_list.insert_at_end(3)
        self.assertEqual(self.linked_list.tail.data, 3)
        self.linked_list.insert_at_end(4)
        self.assertEqual(self.linked_list.tail.data, 4)

    def test_search(self):
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(6)
        self.assertTrue(self.linked_list.search(5))
        self.assertFalse(self.linked_list.search(7))

    def test_remove_at_beginning(self):
        self.linked_list.insert_at_end(8)
        self.linked_list.insert_at_end(9)
        removed_data = self.linked_list.remove_at_beginning()
        self.assertEqual(removed_data, 8)
        self.assertEqual(self.linked_list.head.data, 9)

    def test_remove_at_end(self):
        self.linked_list.insert_at_end(10)
        self.linked_list.insert_at_end(11)
        removed_data = self.linked_list.remove_at_end()
        self.assertEqual(removed_data, 11)
        self.assertEqual(self.linked_list.tail.data, 10)

    def test_remove_at(self):
        self.linked_list.insert_at_end(12)
        self.linked_list.insert_at_end(13)
        self.linked_list.insert_at_end(14)
        removed_data = self.linked_list.remove_at(13)
        self.assertEqual(removed_data, 13)
        self.assertFalse(self.linked_list.search(13))

if __name__ == '__main__':
    unittest.main()