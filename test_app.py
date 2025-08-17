from app import add
from app import multi

def test_add():
    assert add(2, 3) == 5

def test_mulit():
    assert multi(2, 3) == 6
