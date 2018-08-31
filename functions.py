# Functions that build functions:

def get_add_N(N):
    """
    Symbol: ' +N'
    """
    return lambda x: x + N


def get_subtract_N(N):
    """
    Symbol: ' -N'
    """
    return lambda x: x - N


def get_multiply_by_N(N):
    """
    Symbol: ' *N'
    """
    return lambda x: x * N


def get_right_insert_N(N):
    """
    Symbol: '..N'
    """
    def fn(x):
        digits = list(str(x))
        digits.append(str(N))
        return int("".join(digits))
    return fn


def get_left_insert_N(N):
    """
    Symbol: 'N..'
    """
    def fn(x):
        digits = list(str(x))
        if digits[0] == '-':
            digits = ['-', str(N)] + digits[1:]
        else:
            digits = [str(N)] + digits
        return int("".join(digits))
    return fn


# 1st order functions:

def reverse(m):
    """
    Symbol: 'rev'
    """
    return int("".join(reversed(list(str(m)))))


def right_shift(m):
    """
    Symbol: '>>>'
    """
    if m > 9:
        return int(str(m)[:-1])
    else:
        return 0


def left_shift(m):
    """
    Symbol: '<<<'
    """
    return m * 10


def flip_sign(m):
    """
    Symbol: '*-1'
    """
    return -1 * m



