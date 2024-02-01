from isbigger import isbigger, issmaller, isequal

def test_isbigger():
    assert isbigger(3, 2) == True
    assert isbigger(2, 3) == False
    assert isbigger(2, 2) == False

def test_issmaller():
    assert issmaller(3, 2) == False
    assert issmaller(2, 3) == True
    assert issmaller(2, 2) == False

def test_isequal():
    assert isequal(3, 2) == False
    assert isequal(2, 3) == False
    assert isequal(2, 2) == True