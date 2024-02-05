from is_bigger.functions import isBigger, isSmaller, isEqual, isNotBigger, isNotSmaller, isNotEqual

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

def test_isnotbigger():
    assert isNotBigger(3, 2) == False
    assert isNotBigger(2, 3) == True
    assert isNotBigger(2, 2) == True

def test_isnotsmaller():
    assert isNotSmaller(3, 2) == True
    assert isNotSmaller(2, 3) == False
    assert isNotSmaller(2, 2) == True

def test_isnotequal():
    assert isNotEqual(3, 2) == True
    assert isNotEqual(2, 3) == True
    assert isNotEqual(2, 2) == False