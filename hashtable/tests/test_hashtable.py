
from hashtable.hashtable import Hashtable , leftJoin

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

def test_keys():
    hashtable = Hashtable()
    hashtable.set('A' , 'First letter')
    hashtable.set('A' , 'a is the small of it')
    hashtable.set('B' , 'secound letter')
    hashtable.set('B' , 'b is the small of it')
    hashtable.set('Z' , 'last letter')
    hashtable.set('Z' , 'z is the small of it')
    assert hashtable.keys()==  ['B', 'B', 'A', 'A', 'Z', 'Z']

def test_leftJoin():
    hashtable1 = Hashtable()
    hashtable2 = Hashtable()
    hashtable1.set('A' , 'First letter')
    hashtable2.set('A' , 'a is the small of it')
    hashtable1.set('B' , 'secound letter')
    hashtable2.set('B' , 'b is the small of it')
    hashtable1.set('Z' , 'last letter')
    hashtable2.set('Z' , 'z is the small of it')
    assert leftJoin(hashtable1, hashtable2)==  {'B': ['secound letter', 'b is the small of it'], 'A': ['First letter', 'a is the small of it'], 'Z': ['last letter', 'z is the small of it']}


def test_delete():
    hashtable = Hashtable()
    hashtable.set("Django", "python")
    hashtable.delete("Django")
    actual = hashtable.get("Django")
    expected = None
    actual == expected

