from models.rectangle import Rectangle


import unittest


class test_Rectangle(unittest.TestCase):
    def setUp(self):
        self.obj1 = Rectangle(5, 10)
        self.obj2 = Rectangle(2, 4, 0, 0, 100)

    def test_id(self):
        #self.assertEqual(self.obj1.id, 1)
        self.assertNotEqual(self.obj1.id, self.obj2.id)
        self.assertEqual(self.obj2.id, 100)

    def test_getter(self):
        self.assertEqual(self.obj1.width, 5)
        self.assertEqual(self.obj1.height, 10)
        self.assertEqual(self.obj1.x, 0)
        self.assertEqual(self.obj1.y, 0)

    def test_setter(self):
        self.obj1.width = 6
        self.obj1.height = 12
        self.obj1.x = 1
        self.obj1.y = 1
        self.assertEqual(self.obj1.width, 6)
        self.assertEqual(self.obj1.height, 12)
        self.assertEqual(self.obj1.x, 1)
        self.assertEqual(self.obj1.y, 1)

    def test_height_and_width_exceptions(self):
        with self.assertRaises(Exception) as assert_error:
            self.obj1.height = "11"
        self.assertEqual(assert_error.exception.args[0], "height must be an integer")

        with self.assertRaises(Exception) as assert_error:
            self.obj1.width = [1, 2, 4]
        self.assertEqual(assert_error.exception.args[0], "width must be an integer")

        with self.assertRaises(Exception) as assert_error:
            self.obj1.height = -1
        self.assertEqual(assert_error.exception.args[0], "height must be > 0")

        with self.assertRaises(Exception) as assert_error:
            self.obj1.width = -1
        self.assertEqual(assert_error.exception.args[0], "width must be > 0")

    def test_x_and_y_exceptions(self):
        with self.assertRaises(Exception) as assert_error:
            self.obj1.x = (1, "two", 33.33)
        self.assertEqual(assert_error.exception.args[0], "x must be an integer")

        with self.assertRaises(Exception) as assert_error:
            self.obj1.y = float('nan')
        self.assertEqual(assert_error.exception.args[0], "y must be an integer")

        with self.assertRaises(Exception) as assert_error:
            self.obj1.x = -10
        self.assertEqual(assert_error.exception.args[0], "x must be >= 0")

        with self.assertRaises(Exception) as assert_error:
            self.obj1.y = -3
        self.assertEqual(assert_error.exception.args[0], "y must be >= 0")


    def tearDown(self):
        del self.obj1
        del self.obj2


if __name__ == "__main__":
    unittest.main()
