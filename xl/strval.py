from value import Value


class StrVal(Value):
    ADD = "&"

    def __init__(self, value):
        super(StrVal, self).__init__(value)
        self.value = '"%s"' % self.value  # needs to be in double quotes
