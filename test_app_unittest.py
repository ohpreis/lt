import unittest
import app


class TestAPP(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_list(self):
        self.assertIsInstance(app.get_the_json(1), list)

    def test_version(self):
        self.assertTrue(app.check_required_version())


if __name__ == '__main__':
    unittest.main()