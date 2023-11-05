from seasons import birth
import pytest

def test_valid_dates():
    assert birth('1999-12-12') == '1999-12-12'
    assert birth('2023-10-07') == '2023-10-07'

def test_invalid_dates():
    with pytest.raises(SystemExit) as sample:
        birth('3999-12-12')
    assert sample.type == SystemExit

    with pytest.raises(SystemExit) as sample:
        birth('1999-13-12')
    assert sample.type == SystemExit
    with pytest.raises(SystemExit) as sample:
        birth('1999-12-32')
    assert sample.type == SystemExit

