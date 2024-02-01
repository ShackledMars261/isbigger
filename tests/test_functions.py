from is_bigger.functions import isBigger, isSmaller, isEqual

def test_isbigger():
    assert isBigger(3, 2) == True
    assert isBigger(2, 3) == False
    assert isBigger(2, 2) == False

def test_issmaller():
    assert isSmaller(3, 2) == False
    assert isSmaller(2, 3) == True
    assert isSmaller(2, 2) == False

def test_isequal():
    assert isEqual(3, 2) == False
    assert isEqual(2, 3) == False
    assert isEqual(2, 2) == True