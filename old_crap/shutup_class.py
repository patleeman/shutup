import sys


class ShutUpWrite(object):
    """
    Mock sys.stdout object with a nuked write method.  Probably not healthy.
    """
    def write(self, text):
        pass


class shutup(object):
    def __init__(self, function=None, *args, **kwargs):
        self.save_stdout = sys.stdout

    def _shutup(self, function):
        sys.stdout = ShutUpWrite()
        output = function()
        sys.stdout = self.save_stdout
        return output

    def _shutup_decorator(self):

        """
        decorator use case
        @shutup
        def some_function():
            do some stuff
        """
        def new_fn():
            stdout_save = sys.stdout
            sys.stdout= ShutUpWrite()
            output = function()
            sys.stdout = stdout_save
            return(output)
        return(new_fn)

    '''
    def __call__(self, function=None):
        if function is None:
            return self._shutup_decorator
        elif function is not None:
            return self._shutup(function)
    '''
    def __enter__(self):
        """
        Context manager use case.
        with shutup:
            run some code
        """
        sys.stdout = ShutUpWrite()
        return None

    def __exit__(self, type, value, traceback):
        sys.stdout = self.save_stdout
        return None
