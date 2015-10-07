# Ripped from http://stackoverflow.com/questions/2828953/silence-the-stdout-of-a-function-in-python-without-trashing-sys-stdout-and-resto

import sys
import contextlib

# Mock sys.stdout object with a negated write method.
class ShutUpWrite(object):
    def write(self, text):
        pass

@contextlib.contextmanager
def shutup_context():
    stdout_save = sys.stdout
    sys.stdout= ShutUpWrite()
    yield
    sys.stdout = stdout_save

def shutup_fn(fn):
    stdout_save = sys.stdout
    sys.stdout= ShutUpWrite()
    output = fn()
    sys.stdout = stdout_save
    return(output)

def shutup(fn=None):
    if fn is None:
        return shutup_context()
    elif fn is not None:
        return shutup_fn(fn)

shutup = shutup()