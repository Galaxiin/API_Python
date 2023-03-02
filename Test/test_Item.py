import unittest
import sys
sys.path.append('')

from Data import Item

class TestItem(unittest.TestCase):
    def test_create_item(self):
        # Test de la validation 
        item = Item(id=1, name="John", age=30, address="123 Main St", mail="john@example.com")
        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "John")
        self.assertEqual(item.age, 30)
        self.assertEqual(item.address, "123 Main St")
        self.assertEqual(item.mail, "john@example.com")

    def test_create_item_invalid_data(self):
        # Test creating a new item with invalid data
        with self.assertRaises(TypeError):
            # Missing required arguments
            item = Item()
        with self.assertRaises(TypeError):
            # Invalid data types
            item = Item(id="1", name=123, age="30", address=123, mail=True)

    def test_generate_id(self):
        # Test generating a new ID for an item
        # Since the generate_id method is currently empty, this test will always fail
        item1 = Item(id=Item.generate_id(), name="John", age=30, address="123 Main St", mail="john@example.com")
        item2 = Item(id=Item.generate_id(), name="Jane", age=25, address="456 Main St", mail="jane@example.com")
        self.assertNotEqual(item1.id, item2.id)

if __name__ == '__main__':
    unittest.main()