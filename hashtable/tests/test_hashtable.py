from pyparsing import java_style_comment
from hashtable.hashtable import Hashtable

def test_get():

    hashtable = Hashtable()
    hashtable.set("Django", "python")
    actual = hashtable.get("Django")
    expected = "python"
    assert actual == expected

def test_get2():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    hashtable.set("ognajD", "nohtyp")
    actual = hashtable.get("Django")
    expected = "python"
    assert actual == expected

def test_get3():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    hashtable.set("ognajD", "nohtyp")
    actual = hashtable.get("ognajD")
    expected = "nohtyp"
    assert actual == expected

def test_get4():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    actual = hashtable.get("Djang")
    expected = None
    assert actual == expected

def test_contains():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    actual = hashtable.contains("Django")
    expected = True
    assert actual == expected

def test_contains2():
    hashtable = Hashtable()
    actual = hashtable.contains("ayat")
    expected = False
    assert actual == expected


def test_hash():
    hashtable = Hashtable()
    actual = hashtable.hash("ayat")
    expected = 773
    assert actual == expected

def test_hash1():
    hashtable = Hashtable()
    actual = hashtable.hash(75)
    expected = 676
    assert actual == expected

def test_delete():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    hashtable.delete("Django")
    actual = hashtable.get("Django")
    expected = None
    actual == expected

