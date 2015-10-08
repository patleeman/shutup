# Ripped from http://stackoverflow.com/questions/2828953/silence-the-stdout-of-a-function-in-python-without-trashing-sys-stdout-and-resto

import sys
import contextlib

# Mock sys.stdout object with a negated write method.
class ShutUpWrite(object):
    def write(self, text):
        pass

# with use case i.e.
# with shutup:
#     run some code
@contextlib.contextmanager
def shutup_context():
    stdout_save = sys.stdout
    sys.stdout= ShutUpWrite()
    try:
        yield
    finally:
        sys.stdout = stdout_save

# decorator use case i.e.
# @shutup
# def some_function():
def shutup_decorator(fn):
    def new_fn():
        return shutup_basic(fn)
    return(new_fn)

# wrapper use case i.e. shutup(some_function)
def shutup_basic(fn):
    stdout_save = sys.stdout
    sys.stdout= ShutUpWrite()
    output = fn()
    sys.stdout = stdout_save
    return(output)

def shutup(fn=None):
    if fn is None:
        print("FN IS NONE - Running with context manager")
        return shutup_context()
    else:
        print("FN IS NOT NONE - Running as decorator")
        decorator = shutup_decorator(fn)
        return decorator
