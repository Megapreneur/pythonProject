import unittest

from Account import shopping


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("I run before")

    def tearDown(self) -> None:
        print("I run after")


    def test_something(self):
        print("I'm running")


if __name__ == '__main__':
    unittest.main()
