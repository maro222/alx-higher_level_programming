from models.base import Base

import unittest

class test_Base(unittest.TestCase):

    def setUp(self):
        print("set up")
        self.obj1 = Base(12)
        self.obj2 = Base(13)

    def test_no_id(self):
        self.obj3 = Base()
        self.assertEqual(self.obj3.id, 1)
        self.obj4 = Base()
        self.assertEqual(self.obj4.id, 2)

    def test_id(self):
        self.assertEqual(self.obj1.id, 12)
        self.assertEqual(self.obj2.id, 13)
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def tearDown(self):
        del self

if __name__ == "__main__":
    unittest.main()
