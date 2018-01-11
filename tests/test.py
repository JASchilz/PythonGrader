import unittest


class DemonstrationTestCase(unittest.TestCase):
    """
    This set of demonstration tests should generate a BAD report, because
    `test_fails` will fail.
    
    These tests are provided so that you may run the command:
    `python main.py PythonGrader users.txt.example`
    """

    def test_passes(self):
        self.assertTrue(True)

    def test_fails(self):
        self.assertEqual(3, 1+1)

if __name__ == '__main__':
    unittest.main()
