from bank import value

def test_hello():
    assert value('hello') == 0
def test_hello_upper():
    assert value('HELLO') == 0
def test_h_only():
    assert value('haribo') == 20
def test_h_only_upper():
    assert value('HARIBO') == 20
def test_different():
    assert value('Good morning') == 100