from c import C


class Func(C):
    def __init__(self, name, args_cmp_func=None, doc=None):
        self.name = name
        self.args_cmp_func = args_cmp_func

        if doc:
            self.__doc__ = doc

    def __call__(self, *args, **kwargs):
        if self.args_cmp_func:
            assert self.args_cmp_func(args), self.args_cmp_func.__doc__

        return '={}({})'.format(
            self.name, ', '.join([str(a).lstrip('=') for a in args]))

    def help(self):
        return self.__doc__
