import shutup
import sys
import unittest

class TestShutUp(unittest.TestCase):
    def setUp(self):
        print("Control Control Control")
        sys.stdout.write("Control Control Control")

    @staticmethod
    @shutup.shutup
    def yammering_decorated():
        print("BLAH BLAH BLAH")
        print("WAH WAH WAH")
        sys.stdout.write("HELLLLOOOO")
        sys.stdout.write("HEYYY THEREE!!")
        return 2 + 2

    def test_decorated(self):
        result = self.yammering_decorated()
        self.assertEqual(result, 4)

    @staticmethod
    def yammering_context():
        print("BLAH BLAH BLAH")
        print("WAH WAH WAH")
        sys.stdout.write("HELLLLOOOO")
        sys.stdout.write("HEYYY THEREE!!")
        return 2+2

    def test_context(self):
        with shutup.shutup:
            result = self.yammering_context()
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()