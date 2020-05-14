import unittest
import mypackage

class TestFunc(unittest.TestCase):
    def test_func(self):
        self.assertEqual(mypackage.myfunc(),1)

if __name__ == '__main__':
    unittest.main()

