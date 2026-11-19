def square(x: int | float) -> int | float:
    res = x ** 2
    return res


def pow(x: int | float) -> int | float:
    res = x ** x
    return res


def outer(x: int | float, function) -> object:
    """ Function that stores a value. To make multiple Operations on.
    """
    count = 0

    # outer function: takes 'x'  and 'function'and defines inner_function
    def inner() -> float:
        """ x, count and function are remembered from outer

        Returns:
            float
        """
        nonlocal count
        # check if its the first occurence
        # modify outer value
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
