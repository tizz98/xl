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
        from f import F
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
