from hashtable.hashtable import Hashtable

def test_get():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    actual = hashtable.get("Django")
    expected = 17
    assert actual == expected


def test_contains():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    actual = hashtable.contains("Django")
    expected = True
    assert actual == expected

def test_contains2():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    actual = hashtable.contains("ayat")
    expected = False
    assert actual == expected


def test_hash():
    hashtable = Hashtable()
    actual = hashtable.hash("ayat")
    expected = 773
    assert actual == expected