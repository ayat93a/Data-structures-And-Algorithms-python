
from tree.tree import Binary_search_tree , BinaryTree, TNode , Breadth_first

# from stack_and_queue.queue import Queue

def test_empty_tree():
    actual = print(BinaryTree())
    expected = None
    assert actual == expected
 
def test_single_node():
    node1 = TNode('A')
    tree = Binary_search_tree()
    tree.root = node1
    actual = tree.Pre_order_rec()
    expected = ['A']
    assert expected ==  actual

def test_single_node1():
    node1 = TNode('A')
    tree = Binary_search_tree()
    tree.root = node1
    actual = tree.In_order_rec()
    expected = ['A']
    assert expected ==  actual

def test_single_node2():
    node1 = TNode('A')
    tree = Binary_search_tree()
    tree.root = node1
    actual = tree.Post_ord_rec()
    expected = ['A']
    assert expected ==  actual

def test_add_left():
    node1 = TNode('A')
    node2 = TNode('B')
    tree = Binary_search_tree()
    tree.root = node1
    node1.left = node2
    actual = tree.Pre_order_rec()
    expected = ['A' , 'B']
    assert expected ==  actual

def test_add_left2():
    node1 = TNode('A')
    node2 = TNode('B')
    tree = Binary_search_tree()
    tree.root = node1
    node1.left = node2
    actual = tree.In_order_rec()
    expected = ['B' , 'A']
    assert expected ==  actual

def test_add_left3():
    node1 = TNode('A')
    node2 = TNode('B')
    tree = Binary_search_tree()
    tree.root = node1
    node1.left = node2
    actual = tree.Post_ord_rec()
    expected = ['B' , 'A']
    assert expected ==  actual

def test_add_right():
    node1 = TNode('A')
    node2 = TNode('B')
    tree = BinaryTree()
    tree.root = node1
    node1.right = node2
    actual = tree.Pre_order_rec()
    expected = ['A' , 'B']
    assert expected ==  actual

def test_add_right2():
    node1 = TNode('A')
    node2 = TNode('B')
    tree = BinaryTree()
    tree.root = node1
    node1.right = node2
    actual = tree.In_order_rec()
    expected = ['A' , 'B']
    assert expected ==  actual

def test_add_right3():
    node1 = TNode('A')
    node2 = TNode('B')
    tree = BinaryTree()
    tree.root = node1
    node1.right = node2
    actual = tree.Post_ord_rec()
    expected = ['B', 'A']
    assert expected ==  actual

def test_Pre_order_rec():
    node1 = TNode('A')
    node2 = TNode('B')
    node3 = TNode('C')
    node4 = TNode('D')
    node5 = TNode('E')
    node6=TNode('F')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    tree = BinaryTree()
    tree.root = node1
    actual = tree.Pre_order_rec()
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert expected ==  actual

def test_In_order_rec():
    node1 = TNode('A')
    node2 = TNode('B')
    node3 = TNode('C')
    node4 = TNode('D')
    node5 = TNode('E')
    node6=TNode('F')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    tree = BinaryTree()
    tree.root = node1
    actual = tree.In_order_rec()
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert expected ==  actual

def test_Post_ord_rec():
    node1 = TNode('A')
    node2 = TNode('B')
    node3 = TNode('C')
    node4 = TNode('D')
    node5 = TNode('E')
    node6=TNode('F')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    tree = BinaryTree()
    tree.root = node1
    actual = tree.Post_ord_rec()
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert expected ==  actual

def test_add():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.In_order_rec()
    expected = [1, 5, 7, 9, 12, 15, 20, 25, 30, 40]
    assert expected ==  actual

def test_add1():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.root.value
    expected= 20
    assert expected ==  actual

def test_add2():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.root.left.value
    expected= 5
    assert expected ==  actual

def test_add3():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.root.left.left.value
    expected= 1
    assert expected ==  actual

def test_add4():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.root.right.value
    expected= 30
    assert expected ==  actual

def test_add5():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.root.right.right.value
    expected= 40
    assert expected ==  actual


def test_Contains():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.Contains(1)
    expected = True
    assert expected ==  actual

def test_Contains1():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.Contains(100)
    expected = False
    assert expected ==  actual

def test_Contains2():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.Contains(20)
    expected = True
    assert expected ==  actual

def test_Contains3():
    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)
    actual = binary_search_tree.Contains(7)
    expected = True
    assert expected ==  actual

def test_Breadth_first():
    tree = BinaryTree()
    node1 = TNode('A')
    tree.root = node1
    node2 = TNode('B')
    node3 = TNode('C')
    node4 = TNode('D')
    node5 = TNode('E')
    node6=TNode('F')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    actual = Breadth_first(tree)
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    assert expected ==  actual


def test_Breadth_first1():
    tree = BinaryTree()
    node1 = TNode('A')
    tree.root = node1
    actual = Breadth_first(tree)
    expected = ['A']
    assert expected ==  actual

def test_Breadth_first2():
    tree = BinaryTree()
    node1 = TNode('A')
    tree.root = node1
    node2 = TNode('B')
    node3 = TNode('C')
    node1.left = node2
    node1.right = node3
    actual = Breadth_first(tree)
    expected = ['A', 'B', 'C' ]
    assert expected ==  actual

def test_Breadth_first3():
    tree = BinaryTree()
    node1 = TNode('A')
    tree.root = node1
    node3 = TNode('C')
    node1.right = node3
    actual = Breadth_first(tree)
    expected = ['A', 'C' ]
    assert expected ==  actual

def test_Breadth_first4():
    tree = BinaryTree()
    node1 = TNode('A')
    tree.root = node1
    node2 = TNode('B')
    node1.left = node2
    actual = Breadth_first(tree)
    expected = ['A', 'B']
    assert expected ==  actual