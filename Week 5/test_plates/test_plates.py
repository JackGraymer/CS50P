from plates import is_valid

def test_empty():
    assert is_valid('') == False
def test_too_short():
    assert is_valid('a') == False
def test_long():
    assert is_valid('1234567') == False
def test_all_numbers():
    assert is_valid('123456') == False
def test_all_letters():
    assert is_valid('asd.,?') == False
def test_first_non_0():
    assert is_valid('AAA012') == False
def test_no_number_middle():
    assert is_valid('AAA22A') == False
