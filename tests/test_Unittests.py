#!/usr/bin/python3

import unittest
from my_module import MyClass, my_function

class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.obj = MyClass("Test Object")

    def test_get_name(self):
        self.assertEqual(self.obj.get_name(), "Test Object")

    def test_set_name(self):
        self.obj.set_name("New Object")
        self.assertEqual(self.obj.get_name(), "New Object")


class TestMyFunction(unittest.TestCase):
    def test_my_function(self):
        # Redirect stdout to capture the printed message
        import sys
        from io import StringIO
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        my_function()

        sys.stdout = old_stdout

        self.assertEqual(captured_output.getvalue().strip(), "This is a sample function.")

if __name__ == '__main__':
    unittest.main()
