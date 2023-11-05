from um import count

def test_count_valid():
    assert count('umbrella') == 0
    assert count('entiendo, um, umbrella') == 1
    assert count('um, um! um? um') == 4
    assert count('Horacium, stadium') == 0
    assert count('Umberto, stadium') == 0
    assert count('Um, Horacium, stadium') == 1