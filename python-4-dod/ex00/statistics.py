from typing import Any


def median(nums: list[float]) -> float:
    """ Returns the median value od a given lsit

    Args:
        nums (list[float]): List of floats
    """
    numscp = nums.copy()
    numscp.sort()
    n = len(numscp)
    if n % 2 == 0:
        res = (numscp[n//2 - 1] + numscp[n//2]) / 2
    else:
        res = (numscp[n//2])
    return res


def mean(nums: list[float]) -> float:
    """ Takes a list an prints the mean value

    Args:
        nums (list[float]): List of floats
    """
    res = 0
    n = len(nums)
    if n == 0:
        raise ValueError("List is empty")

    for i in nums:
        res = res + i

    res = res / n

    return res


def quartile(nums: list[float]) -> tuple[float, float]:

    cp = sorted(nums)

    if len(cp) == 0:
        raise ValueError("List is empty")

    n = len(cp)
    mid = n // 2

    if n % 2 == 0:
        left = cp[:mid]
        right = cp[mid:]
    else:
        left = cp[:mid]
        right = cp[mid + 1:]

    q1 = median(left)
    q3 = median(right)

    return (q1, q3)


def var(nums: list[float]) -> float:
    """ Calculates the standard Deviation

    Args:
        nums (list[float])

    Returns:
        float
    """
    mean1 = mean(nums)
    n = len(nums)

    res = [mean1-x for x in nums]

    res = [x**2 for x in res]
    final = 0
    for i in res:
        final += i
    final = final / n

    return final


def std(nums: list[float]) -> None:
    variance = var(nums)
    res = variance ** 0.5
    return res


def ft_statistics(*args: Any, **kwargs: Any) -> None:

    # check for non numeric numbers in args 
    numbers = []
    for arg in args:
        numbers.append(float(arg))

    for value in kwargs.values():
        if value == "mean":
            res = mean(numbers)
            print(res)
        elif value == "median":
            res = median(numbers)
            print(res)
        elif value == "quartile":
            res = quartile(numbers)
            print(res)
        elif value == "std":
            res = std(numbers)
            print(res)
        elif value == "var":
            res = var(numbers)
            print(res)
        else:
            print("ERROR")
