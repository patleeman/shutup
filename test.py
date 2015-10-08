import shutup
import sys
import unittest

class TestShutUp(unittest.TestCase):
    def setUp(self):
        print("Control print case, this should print.")


    @staticmethod
    @shutup.shutup
    def yammering_decorated():
        print("garbage garbage garbage")
        print("garbage garbage garbage")
        sys.stdout.write("garbage garbage garbageO")
        sys.stdout.write("garbage garbage garbage")
        return 2 + 2

    def test_decorated(self):
        result = self.yammering_decorated()
        self.assertEqual(result, 4)

    @staticmethod
    def yammering_context():
        print("garbage garbage garbage")
        print("garbage garbage garbage")
        sys.stdout.write("garbage garbage garbage")
        sys.stdout.write("garbage garbage garbage")
        return 2+2

    def test_context(self):
        with shutup.shutup:
            result = self.yammering_context()
        self.assertEqual(result, 4)


    @staticmethod
    def yammering_mute():
        a = 1
        shutup.mute()
        print("BLAH BLAH BLAH")
        sys.stdout.write("DUR DUR DUR")
        a += 1
        shutup.unmute()
        a += 1
        return a

    def test_mute(self):
        self.assertEqual(self.yammering_mute(), 3)
if __name__ == '__main__':
    unittest.main()