from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.1.1") == True
    assert validate("127.0.0.1") == True
    assert validate("10.0.0.1") == True

def test_invalid_ipv4():
    assert validate("cat") == False
    assert validate("250") == False
    assert validate("251.") == False
    assert validate("251.251.251.251.1") == False
    assert validate("1.1.1.256") == False
    assert validate("1.1.256.1") == False
    assert validate("1.256.1.1") == False
    assert validate("256.1.1.1") == False