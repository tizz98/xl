from c import C


class Cell(C):
    def __init__(self, column, row=None, sheet=None):
        self.column = column.upper()
        self.row = row or ''
        self.sheet = sheet

    def __str__(self):
        base = '{}{}'.format(self.column, self.row)
        if self.sheet:
            # needs to be in single quotes
            return "'{}'!{}".format(self.sheet, base)
        return base

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self)
