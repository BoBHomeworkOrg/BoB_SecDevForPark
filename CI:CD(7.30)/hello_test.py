import unittest
import hello


class TestHello(unittest.TestCase):
    def test_add(self):
        instance = hello.Hello()
        result = instance.add(2, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
