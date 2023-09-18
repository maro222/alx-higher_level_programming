from models.base import Base
from models.rectangle import Rectangle
import unittest
import io
import sys

class test_Rectangle(unittest.TestCase):
    def setUp(self):
        self.obj1 = Rectangle(3, 6, 0, 0, 200)
        self.obj2 = Rectangle(2, 4, 0, 0, 100)

    def test_id(self):
        self.tempobj = Rectangle(5, 10)
        self.assertEqual(self.tempobj.id, 1)

        self.assertEqual(self.obj1.id, 200)
        self.assertNotEqual(self.obj1.id, self.obj2.id)
        self.assertEqual(self.obj2.id, 100)

    def test_getter(self):
        self.assertEqual(self.obj1.width, 3)
        self.assertEqual(self.obj1.height, 6)
        self.assertEqual(self.obj1.x, 0)
        self.assertEqual(self.obj1.y, 0)

    def test_setter(self):
        self.obj1.width = 5
        self.obj1.height = 10
        self.obj1.x = 1
        self.obj1.y = 1
        self.assertEqual(self.obj1.width, 5)
        self.assertEqual(self.obj1.height, 10)
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

    def test_area(self):
        self.assertEqual(self.obj1.area(), 3 * 6)
        self.assertEqual(self.obj2.area(), 2 * 4)

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display(self):
        capture = test_Rectangle.capture_stdout(self.obj1, "display")
        correct = "###\n###\n###\n###\n###\n###\n"
        self.assertEqual(correct, capture.getvalue())

    def tearDown(self):
        del self.obj1
        del self.obj2


if __name__ == "__main__":
    unittest.main()
