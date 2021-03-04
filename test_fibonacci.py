import unittest
import fibonacci as f

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(f.fib(11),89)

    def test2(self):
        self.assertEqual(f.fib(20),6765)
    
    def test3(self):
        self.assertEqual(f.fib(0),0)

    def test4(self):
        self.assertEqual(f.fib(1),1)

if __name__ == '__main__':
    unittest.main()