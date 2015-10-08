import sys

# Mock sys.stdout object with a negated write method.
class ShutUpWrite(object):
    def write(self, text):
        pass


class shutup(object):
    def __init__(self, function=None, *args, **kwargs):
        self.save_stdout = sys.stdout

        if function is not None:
            self._shutup(function)

    def _shutup(self, function):
        sys.stdout = ShutUpWrite()
        output = function()
        sys.stdout = self.save_stdout
        return output

    def __call__(self, function):
        is_fn = hasattr(function, '__call__')
        print(is_fn)
        return self._shutup(function)

    def __enter__(self):
        sys.stdout = ShutUpWrite()
        return None

    def __exit__(self, type, value, traceback):
        sys.stdout = self.save_stdout
        return None
