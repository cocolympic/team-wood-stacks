def add(a, b):
    """
    Add two numbers together.

    >>> add(1, 2)
    3
    """
    return a + b


if __name__ == "__main__":
    import doctest
    print("doctest.testmod() passed: ", doctest.testmod())