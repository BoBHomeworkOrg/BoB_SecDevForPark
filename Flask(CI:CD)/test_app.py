import unittest
import app

class TestHello(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
    
    def test_add(self):
        test = {'a': 1, 'b': 2}
        res = self.app.get('/add', query_string=test)
        res = res.get_data().decode()
        self.assertEqual(str(3), res)
    
    def test_sub(self):
        test = {'a': 1, 'b': 2}
        res = self.app.get('/sub', query_string=test)
        res = res.get_data().decode()
        self.assertEqual(str(-1), res)

if __name__ == "__main__":
    unittest.main()
    
