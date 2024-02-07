from is_bigger.mlfunctions import ml_is_bigger, ml_is_smaller, ml_is_equal, ml_is_not_bigger, ml_is_not_smaller, ml_is_not_equal

def test_ml_is_bigger():
    assert ml_is_bigger(3, 2) == True
    assert ml_is_bigger(2, 3) == False
    assert ml_is_bigger(2, 2) == False

def test_ml_is_smaller():
    assert ml_is_smaller(2,3) == True
    assert ml_is_smaller(3,2) == False
    assert ml_is_smaller(2,2) == False

def test_ml_is_equal():
    assert ml_is_equal(3, 2) == False
    assert ml_is_equal(2, 3) == False
    assert ml_is_equal(2, 2) == True

def test_ml_is_not_bigger():
    assert ml_is_not_bigger(3, 2) == False
    assert ml_is_not_bigger(2, 3) == True
    assert ml_is_not_bigger(2, 2) == True

def test_ml_is_not_smaller():
    assert ml_is_not_smaller(3, 2) == True
    assert ml_is_not_smaller(2, 3) == False
    assert ml_is_not_smaller(2, 2) == True

def test_ml_is_not_equal():
    assert ml_is_not_equal(3, 2) == True
    assert ml_is_not_equal(2, 3) == True
    assert ml_is_not_equal(2, 2) == False