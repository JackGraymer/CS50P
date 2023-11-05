from twttr import shorten

def test_lower():
    assert shorten('aeiou') == ''
    assert shorten('murcielago') == 'mrclg'
def test_caps():
    assert shorten('AEIOU') == ''
    assert shorten('YOU ARISE') == 'Y RS'
def test_numbers():
    assert shorten('we are 3') == 'w r 3'
def test_punctuation():
    assert shorten('so, lets go?') == 's, lts g?'