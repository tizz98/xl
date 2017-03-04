from func import Func


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
