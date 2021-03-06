"""
shutup.py v. 1.0

Shuts up stupid console output when you want some peace and quiet using all the
wrong tricks in the book.
"""

import sys
import unittest

import shutup


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
    @shutup.function
    def yammering_decorated_fn():
        print("garbage garbage garbage")
        print("garbage garbage garbage")
        sys.stdout.write("garbage garbage garbageO")
        sys.stdout.write("garbage garbage garbage")
        return 2 + 2

    def test_decorated2(self):
        result = self.yammering_decorated_fn()
        self.assertEqual(result, 4)


    class derp(object):
        def __init__(self):
            self.output = 2+2

        @shutup.method
        def yammering_decorate_method(self):
            print("garbage garbage garbage")
            print("garbage garbage garbage")
            sys.stdout.write("garbage garbage garbageO")
            sys.stdout.write("garbage garbage garbage")
            return self.output

    def test_decorated_method(self):
        instance = self.derp()
        result = instance.yammering_decorate_method()
        self.assertEqual(result, 4)

    @staticmethod
    def yammering_context():
        print("garbage garbage garbage")
        print("garbage garbage garbage")
        sys.stdout.write("garbage garbage garbage")
        sys.stdout.write("garbage garbage garbage")
        return 2+2

    def test_context(self):
        with shutup.shutup():
            result = self.yammering_context()
        self.assertEqual(result, 4)

    def test_context2(self):
        with shutup.context():
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