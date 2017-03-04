from c import C


class Value(C):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self)
