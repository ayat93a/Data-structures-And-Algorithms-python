
from stack_and_queue.stack_queue_animal_shelter import StackQueueAnimalShelter

def test_create_class():
    shelter = StackQueueAnimalShelter()
    actual = shelter.__str__()
    expected = None
    assert actual == expected

def test_enqueue():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual = shelter.__str__()
    expected = '"{cat:lolo}-> {dog:roro}-> {dog:meme}-> {cat:soso}-> {dog:jojo}-> {dog:jojo}-> NULL"'
    assert actual == expected

def test_dequeue_specific_one():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    shelter.dequeue_specific_one('dog' , 'jojo' )
    actual = shelter.__str__()
    expected = '"{cat:lolo}-> {dog:roro}-> {dog:meme}-> {cat:soso}-> {dog:jojo}-> NULL"'
    assert actual == expected


def test_dequeue_specific_one1():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual = shelter.dequeue_specific_one('dog' , 'jojo' )
    expected = 'dog : jojo is dequeued'
    assert actual == expected

def test_dequeue_specific_one2():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual =shelter.dequeue_specific_one('camel' , 'jojo' )
    expected = None
    assert actual == expected

def test_dequeue_first_one1():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual =shelter.dequeue_first_one('cat')
    expected = 'cat  is dequeued'
    assert actual == expected

def test_dequeue_first_one2():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual =shelter.dequeue_first_one('dog')
    expected = 'dog  is dequeued'
    assert actual == expected

def test_dequeue_first_one3():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    shelter.dequeue_first_one('cat')
    actual = shelter.__str__()
    expected = '"{dog:roro}-> {dog:meme}-> {cat:soso}-> {dog:jojo}-> {dog:jojo}-> NULL"'
    assert actual == expected

def test_dequeue_first_one4():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    shelter.dequeue_first_one('dog')
    actual = shelter.__str__()
    expected = '"{cat:lolo}-> {dog:meme}-> {cat:soso}-> {dog:jojo}-> {dog:jojo}-> NULL"'
    assert actual == expected