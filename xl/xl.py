class C(object):
    # Arithmetic connectors
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    POW = '^'

    MOD = 'MOD'

    AND = 'AND'
    OR = 'OR'

    # Equality
    GT = '>'
    LT = '<'
    GTE = '>='
    LTE = '<='
    EQ = "="
    NE = "<>"

    def _combine(self, other, connector, reversed):
        """
        Parameters
        ----------
        other: Cell
        connector: str
        reversed: bool

        Returns
        -------
        F
        """
        if reversed:
            return F(other, connector, self)
        return F(self, connector, other)

    #############
    # OPERATORS #
    #############

    def __add__(self, other):
        return self._combine(other, self.ADD, False)

    def __sub__(self, other):
        return self._combine(other, self.SUB, False)

    def __mul__(self, other):
        return self._combine(other, self.MUL, False)

    def __truediv__(self, other):
        return self._combine(other, self.DIV, False)

    def __div__(self, other):  # Python 2 compatibility
        return type(self).__truediv__(self, other)

    def __mod__(self, other):
        return self._combine(other, self.MOD, False)

    def __pow__(self, other):
        return self._combine(other, self.POW, False)

    def __and__(self, other):
        return self._combine(other, self.AND, False)

    def __or__(self, other):
        return self._combine(other, self.OR, False)

    def __radd__(self, other):
        return self._combine(other, self.ADD, True)

    def __rsub__(self, other):
        return self._combine(other, self.SUB, True)

    def __rmul__(self, other):
        return self._combine(other, self.MUL, True)

    def __rtruediv__(self, other):
        return self._combine(other, self.DIV, True)

    def __rdiv__(self, other):  # Python 2 compatibility
        return type(self).__rtruediv__(self, other)

    def __rmod__(self, other):
        return self._combine(other, self.MOD, True)

    def __rpow__(self, other):
        return self._combine(other, self.POW, True)

    def __rand__(self, other):
        return self._combine(other, self.AND, True)

    def __ror__(self, other):
        return self._combine(other, self.OR, True)

    #############
    # EQUALITY  #
    #############
    def __gt__(self, other):
        return self._combine(other, self.GT, False)

    def __lt__(self, other):
        return self._combine(other, self.LT, False)

    def __eq__(self, other):
        return self._combine(other, self.EQ, False)

    def __ne__(self, other):
        return self._combine(other, self.NE, False)

    def gte(self, other):
        return self._combine(other, self.GTE, False)

    def lte(self, other):
        return self._combine(other, self.LTE, False)


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


class Value(C):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self)


class StrVal(Value):
    ADD = "&"

    def __init__(self, value):
        super(StrVal, self).__init__(value)
        self.value = '"%s"' % self.value  # needs to be in double quotes


class Range(C):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '{}:{}'.format(self.start, self.end)

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self)


def eq(num):
    def inner(args):
        return len(args) == num

    inner.__doc__ = "Number of arguments must be exactly %s" % num
    return inner


def lt(num):
    def inner(args):
        return len(args) < num

    inner.__doc__ = "Number of arguments must be less than %s" % num
    return inner


def gt(num):
    def inner(args):
        return len(args) > num

    inner.__doc__ = "Number of arguments must be greater than %s" % num
    return inner


def between(lower, upper):
    """Lower and upper are inclusive"""
    def inner(args):
        return lower <= len(args) <= upper

    inner.__doc__ = "Number of arguments must be " \
                    "between (inclusive) %s and %s" % (lower, upper)
    return inner


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


IF = Func('IF',
          args_cmp_func=eq(3),
          doc="IF function. Param 1: Conditional. "
              "Param 2: True Part. Param 3: False Part.")
IFS = Func('IFS', args_cmp_func=between(2, 127*2))
IFERROR = Func('IFERROR', args_cmp_func=eq(2))
SUMIFS = Func('SUMIFS', args_cmp_func=between(2, 127*2))
SUM = Func('SUM', args_cmp_func=between(1, 255))
DATE = Func('DATE', args_cmp_func=eq(3))
YEAR = Func('YEAR', args_cmp_func=eq(1))
MONTH = Func('MONTH', args_cmp_func=eq(1))
DAY = Func('DAY', args_cmp_func=eq(1))
