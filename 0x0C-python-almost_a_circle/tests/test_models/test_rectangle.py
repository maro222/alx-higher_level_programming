from models.rectangle import Rectangle


import unittest


class test_Rectangle(unittest.TestCase):
    def setUp(self):
        self.obj1 = Rectangle(5, 10)
        self.obj2 = Rectangle(2, 4, 0, 0, 100)

    def test_id(self):
        self.assertEqual(self.obj1.id, 2)
        self.assertEqual(self.obj2.id, 100)

    def test_getter(self):
        self.assertEqual(self.obj1.width, 5)
        self.assertEqual(self.obj2.height, 4)

    def test_setter(self):
        self.obj1.width = 8
        self.obj1.x = 1
        self.assertEqual(self.obj1.width, 8)
        self.assertEqual(self.obj1.x, 1)

    def tearDown(self):
        del self


if __name__ == "__main__":
    unittest.main()
