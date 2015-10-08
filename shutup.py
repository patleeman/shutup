import sys
import contextlib


class ShutUpWrite(object):
    """
    Mock sys.stdout object with a nuked write method.  Probably not healthy.
    """
    def write(self, text):
        pass


@contextlib.contextmanager
def shutup_context():
    """
    Context manager use case.
    with shutup:
        run some code
    """
    stdout_save = sys.stdout
    sys.stdout= ShutUpWrite()
    try:
        yield
    finally:
        sys.stdout = stdout_save


def shutup_decorator(fn):
    """
    decorator use case
    @shutup
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


def shutup(fn=None):
    """
    Determines whether or not shutup is being used as a a decorator or as a
    context manager and directs appropriately.
    """
    if fn is None:
        return shutup_context()
    else:
        decorator = shutup_decorator(fn)
        return decorator

shutup = shutup()


# Oh yeah, suck on my global.
stdout_save = sys.stdout

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
    sys.stdout = stdout_save
    return True  # momma always said to give back

