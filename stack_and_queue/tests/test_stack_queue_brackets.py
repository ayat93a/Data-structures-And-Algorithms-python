from stack_and_queue.stack_queue_brackets import validate_brackets

def test_val1():
    assert validate_brackets("{***}") == True

def test_val2():
    assert validate_brackets("(](") == False


