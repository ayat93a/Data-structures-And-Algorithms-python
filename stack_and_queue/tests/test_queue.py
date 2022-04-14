
from stack_and_queue.queue import Queue

def test_enqueue0():
    queue = Queue()
    queue.enqueue(2)
    actual = queue.__str__()
    expected = '"{2}-> NULL"'
    assert actual == expected

    
def test_enqueue1():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    actual = queue.__str__()
    expected = '"{2}-> {5}-> {7}-> NULL"'
    assert actual == expected

def test_dequeue():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    actual = queue.dequeue()
    expected = 2
    assert actual == expected

def test_dequeue1():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    queue.dequeue()
    actual = queue.__str__()
    expected = '"{5}-> {7}-> NULL"'
    assert actual == expected 

def test_dequeue2():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.__str__()
    expected = None
    assert actual == expected 

def test_peek():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    actual = queue.peek()
    expected = 2
    assert actual == expected

def test_peek1():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    queue.peek()
    actual = queue.__str__()
    expected = '"{2}-> {5}-> {7}-> NULL"'
    assert actual == expected

def test_is_empty1():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_is_empty2():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(7)
    actual = queue.is_empty()
    expected = False
    assert actual == expected


def test_empty_queue():
    queue = Queue()
    actual = queue.__str__()
    expected = None
    assert actual == expected

# def test_empty_queue_raise_error ():
#     queue = Queue()
#     actual = queue.__str__()
#     expected = None
#     assert actual == expected