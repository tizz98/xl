from c import C


class F(C):
    def __init__(self, lhs, connector, rhs):
        self.lhs = lhs
        self.connector = connector
        self.rhs = rhs

    def to_string(self):
        if not self.connector.isalpha():
            # basic arithmetic
            return '={} {} {}'.format(self.lhs, self.connector, self.rhs)
        # more advanced function
        return '={}({}, {})'.format(self.connector, self.lhs, self.rhs)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self)

    def __str__(self):
        return self.to_string()

