
from stack_and_queue.stack import Stack ,   Pseudo_queue 

def test_push0():
    stack=Stack()
    stack.push(2)
    actual = stack.__str__()
    expected = '"{2}-> NULL"'
    assert actual == expected

def test_push1():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.__str__()
    expected = '"{7}-> {5}-> {2}-> NULL"'
    assert actual == expected

def test_pop0():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.pop()
    expected = 7
    assert actual == expected

def test_pop1():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.__str__()
    expected = None
    assert actual == expected

def test_empty_stack ():
    stack=Stack()
    actual = stack.__str__()
    expected = None
    assert actual == expected

# def test_empty_stack_raise_error ():
#     stack=Stack()
#     stack.peek()
#     actual = stack.__str__()
#     expected = None
#     assert actual == expected



def test_pop2():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    stack.pop()
    actual = stack.__str__()
    expected = '"{5}-> {2}-> NULL"'
    assert actual == expected


def test_peek():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.peek()
    expected = 7
    assert actual == expected
 
def test_peek2():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    stack.peek()
    actual = stack.__str__()
    expected = '"{7}-> {5}-> {2}-> NULL"'
    assert actual == expected

def test_is_empty1():
    stack=Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_is_empty2():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.is_empty()
    expected = False
    assert actual == expected

def test_queue():
    queue= Pseudo_queue()
    actual = queue.__str__()
    excepted = 'None'
    assert actual == excepted

def test_enqueue():
    queue= Pseudo_queue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    actual = queue.__str__()
    expected = '{5}->{10}->{15}->{20}->None'
    assert actual == expected

def test_dequeue():
    queue= Pseudo_queue()
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(10)
    queue.enqueue(5)
    actual = queue.dequeue()
    expected = 'dequeue value --> 20 '
    assert actual == expected
