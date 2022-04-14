from linked_list.linked_list import LinkedList
import pytest

# @pytest.fixure 
# def ll():
#         pass

def test_create_empty_list():
    ll = LinkedList()
    actual = ll.__str__()
    expected = None
    assert actual == expected


def test_insert_values():
    ll = LinkedList()
    ll.insert_values(['ayat' , 'barakat' , 'alkayed'])
    actual =ll.__str__()
    expected = '"{ayat}-> {barakat}-> {alkayed}-> NULL"'
    # print(actual)
    assert actual == expected


def test_insert_at_beginning():
    ll = LinkedList()
    ll.insert_at_beginning('engineer')
    ll.insert_at_beginning('civil')
    actual =ll.__str__()
    expected = '"{civil}-> {engineer}-> NULL"'
    assert actual == expected



def test_get_length():
    ll = LinkedList()
    ll.insert_at_beginning(['engineer' , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    actual =ll.get_length()
    expected = 4
    assert actual == expected

def test_includest():
    ll = LinkedList()
    ll.insert_values (['ayat' , 'barakat' , 'alkayed' ])
    actual = ll.includes('ayat')
    expected = True
    assert actual == expected

def test_includesf():
    ll = LinkedList()
    ll.insert_values (['ayat' , 'barakat' , 'alkayed' ])
    actual = ll.includes('hi')
    expected = False
    assert actual == expected

# def test_remove_at_index():
#     ll = LinkedList()
#     ll.insert_at_beginning([1000 , 1])
#     ll.insert_at_beginning('civil')
#     ll.insert_at_beginning('ayat')
#     ll.insert_at_beginning('python')
#     ll.remove_at_index(2)
#     actual = ll.__str__()
#     expected = '"{python}-> {ayat}-> {[1000, 1]}-> NULL"'
#     assert actual == expected

# def test_insert_at():
#     ll = LinkedList()
#     ll.insert_at_beginning([1000 , 1])
#     ll.insert_at_beginning('civil')
#     ll.insert_at_beginning('ayat')
#     ll.insert_at_beginning('python')
#     ll.insert_at(0, 'a')
#     actual = ll.__str__()
#     expected = '"{a}-> {python}-> {ayat}-> {civil}-> {[1000, 1]}-> NULL"'
#     assert actual == expected

# add a node to the end of the linked list
def test_append1():
    ll = LinkedList()
    ll.insert_values(['ayat' , 'barakat' , 'alkayed'  ])
    ll.append('28')
    actual =ll.__str__()
    expected = '"{ayat}-> {barakat}-> {alkayed}-> {28}-> NULL"'
    assert actual == expected

# add multiple nodes to the end of a linked list
def test_append2():
    ll = LinkedList()
    ll.insert_values(['ayat' , 'barakat' , 'alkayed'  ])
    ll.append('28')
    ll.append('python')
    ll.append('ASAC')
    actual =ll.__str__()
    expected = '"{ayat}-> {barakat}-> {alkayed}-> {28}-> {python}-> {ASAC}-> NULL"'
    assert actual == expected

# insert after a node in the middle of the linked list
# insert a node after the last node of the linked list
def test_insert_after():
    ll = LinkedList()
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.insert_after('ayat' , '5')
    ll.insert_after([1000 , 1] , 'last')
    actual = ll.__str__()
    expected = '"{python}-> {ayat}-> {5}-> {civil}-> {[1000, 1]}-> {last}-> NULL"'
    assert actual == expected

# insert a node before the first node of a linked list
# insert a node before the first node of a linked list
def test_insert_befor():
    ll = LinkedList()
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.insert_at_beginning(16)
    ll.insert_befor(16 , 'softwear')
    ll.insert_befor('ayat' , 'devs')
    actual = ll.__str__()
    expected = '"{softwear}-> {16}-> {python}-> {devs}-> {ayat}-> {civil}-> NULL"'
    assert actual == expected

def test_remove_by_value():
    ll = LinkedList()
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.remove_by_value('civil')
    ll.remove_by_value('python')
    actual = ll.__str__()
    expected = '"{ayat}-> {[1000, 1]}-> NULL"'
    assert actual == expected
def test_reverse():
    ll = LinkedList()
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.insert_at_beginning('hi')
    ll.reverse()
    actual = ll.__str__()
    excepted = '"{[1000, 1]}-> {civil}-> {ayat}-> {python}-> {hi}-> NULL"'
    assert actual == excepted


def test_kElement():
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(1)
    actual = ll.kElement(2)
    expected = 3
    assert actual == expected

def test_kElement1():
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(1)
    actual = ll.kElement(0)
    expected = 2
    assert actual == expected


# def test_kElement2():
#     ll = LinkedList()
#     ll.insert_at_beginning(2)
#     ll.insert_at_beginning(8)
#     ll.insert_at_beginning(3)
#     ll.insert_at_beginning(1)
#     actual = ll.kElement(6)
#     expected = TypeError
#     assert actual == expected
#  updated