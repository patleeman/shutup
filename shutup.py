"""
shutup.py v. 1.0

Shuts up stupid console output when you want some peace and quiet using all the
wrong tricks in the book.
"""

import sys


class ShutUpWrite(object):
    """
    Mock sys.stdout object with a nuked write method.  Probably not healthy.
    """
    def write(self, text):
        pass


class shutup(object):
    def __init__(self, fn=None):
        self._save = sys.stdout
        self._function = fn

    def __call__(self):
        """
        Used for calling on string
        """
        if self._function is not None:
            try:
                sys.stdout = ShutUpWrite()
                output = self._function()
            finally:
                sys.stdout = self._save
            return output
        else:
            raise Exception("Requires a function to call")

    def __enter__(self):
        sys.stdout = ShutUpWrite()
        return True

    def __exit__(self, type, value, traceback):
        sys.stdout = self._save
        return False


def function(fn):
    """
    decorator use case
    @shutup.function
    def some_function():
        do some stuff
    """
    def new_fn():
        stdout_save = sys.stdout
        sys.stdout= ShutUpWrite()
        output = fn()
        sys.stdout = stdout_save
        return(output)
    return(new_fn)


def method(fn):
    """
    class method usecase
    @shutup.method
    def some_function():
        do some stuff
    """
    def new_fn(self):
        stdout_save = sys.stdout
        sys.stdout= ShutUpWrite()
        output = fn(self)
        sys.stdout = stdout_save
        return(output)
    return(new_fn)


def context():
    """
    Alt for with shutup.shutup()
    usage:

    with shutup.context() as shutit:
        do something
    """
    return shutup()



_save_stdout = sys.stdout  # Oh yeah, suck on my global.
def mute():
    """
    Mutes... fucking... everything.
    """
    sys.stdout= ShutUpWrite()
    return True  # why not?


def unmute():
    """
    I hope this works.
    """
    sys.stdout = _save_stdout
    return True  # momma always said to give back


def string(annoying):
    mute()
    try:
        output = exec(annoying)
    finally:
        unmute()
    return output
