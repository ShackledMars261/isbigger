def isBigger(int1: int, int2: int) -> bool:
    """
    Returns True if int1 is greater than int2, False otherwise
    :param int1: int
    :param int2: int
    :return: True if int1 > int2, False otherwise
    """
    return int1 > int2

def isSmaller(int1: int, int2: int) -> bool:
    """
    Returns True if int1 is less than int2, False otherwise
    :param int1: int
    :param int2: int
    :return: True if int1 < int2, False otherwise
    """
    return int1 < int2

def isEqual(int1: int, int2: int) -> bool:
    """
    Returns True if int1 is equal to int2, False otherwise
    :param int1: int
    :param int2: int
    :return: True if int1 == int2, False otherwise
    """
    return int1 == int2

def isNotBigger(int1: int, int2: int) -> bool:
    """
    Returns True if int1 is not greater than int2, False otherwise
    :param int1: int
    :param int2: int
    :return: True if int1 <= int2, False otherwise
    """
    return isSmaller(int1, int2) or isEqual(int1, int2)

def isNotSmaller(int1: int, int2: int) -> bool:
    """
    Returns True if int1 is not less than int2, False otherwise
    :param int1: int
    :param int2: int
    :return: True if int1 >= int2, False otherwise
    """
    return isBigger(int1, int2) or isEqual(int1, int2)

def isNotEqual(int1: int, int2: int) -> bool:
    """
    Returns True if int1 is not equal to int2, False otherwise
    :param int1: int
    :param int2: int
    :return: True if int1 != int2, False otherwise
    """
    return not isEqual(int1, int2)