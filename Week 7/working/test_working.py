from working import convert
import pytest

def test_valid_format():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_invalid_format():
    #assert convert('9:00 AM 5:00 PM') == ValueError
    with pytest.raises(ValueError):
        convert('9:00 AM 5:00 PM')
    with pytest.raises(ValueError):
        convert('8:60 AM to 4:60 PM')