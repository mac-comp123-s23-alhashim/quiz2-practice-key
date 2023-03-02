"""
Python Developer Name: Amin G. Alhashim
"""


def fibonacci(n: int) -> list:
    """
    Generate the Fibonacci sequence up to a given number

    :param n: the number up to which the Fibonacci sequence will be generated
    :return: a list of numbers making the Fibonacci sequence up to n
    """
    if n == 0:
        return [0]

    if n == 1:
        return [0, 1]

    result = [0, 1]
    while result[-2] + result[-1] <= n:
        result.append(result[-2] + result[-1])

    return result


def test_fibonacci_0() -> None:
    """
    A unit test when the input is 0

    :return: None
    """
    assert fibonacci(0) == [0]


def test_fibonacci_1() -> None:
    """
    A unit test for when the input is 1

    :return:
    """
    assert fibonacci(1) == [0, 1]


def test_fibonacci_2() -> None:
    """
    A unit test for when the input is 2

    :return:
    """
    assert fibonacci(2) == [0, 1, 1, 2]


def test_fibonacci_10() -> None:
    """
    A unit test for when the input is 10
    :return:
    """
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
