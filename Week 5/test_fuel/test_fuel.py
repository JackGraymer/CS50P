from fuel import convert, gauge
import pytest

def test_fractions():
    assert convert('1/4') == 25
def test_non_int():
    with pytest.raises(ValueError):
        convert('a/b')
        convert ('5/4')
def test_non_0():
    with pytest.raises(ZeroDivisionError):
        convert('0/0')

def test_percentage():
    assert gauge(25) == '25%'
def test_full():
    assert gauge(99) == 'F'
def test_empty():
    assert gauge(1) == 'E'
