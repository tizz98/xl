from c import C


class Range(C):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '{}:{}'.format(self.start, self.end)

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self)

