from pytest import fixture
import pytest
from tree_intersection import tree_intersection , converter , BinaryTree, TNode

@pytest.fixture
def tree1():
    tree1= BinaryTree ()
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5 = TNode(5)
    node6=TNode(6)
    node7 = TNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    node4.left = node7
    tree1.root = node1 

    return tree1 

@pytest.fixture
def tree2():
    tree2 =BinaryTree()
    node10 = TNode(8)
    tree2.root = node10 
    node20= TNode(5)
    node30 = TNode(10)
    node40 = TNode(3)
    node50 = TNode(2)
    node60=TNode(6)
    node70 = TNode(100)

    node10.left = node20
    node10.right = node30
    node20.left = node40
    node20.right= node50
    node30.left= node60
    node40.left = node70

    return tree2

@pytest.fixture
def tree3():
    tree3 =BinaryTree()
    node10 = TNode(29)
    tree3.root = node10 
    node20= TNode(53)
    node30 = TNode(49)
    node40 = TNode(33)
    node50 = TNode(2)
    node60=TNode(68)
    node70 = TNode(1)

    node10.left = node20
    node10.right = node30
    node20.left = node40
    node20.right= node50
    node30.left= node60
    node40.left = node70

    return tree3

@pytest.fixture
def tree4():
    tree4 =BinaryTree()

    return tree4

def test_traverse1(tree1):
    assert tree1.Pre_order_rec() == [1, 2, 4, 7, 5, 3, 6]

def test_traverse2(tree2):
    assert tree2.Pre_order_rec() ==  [8, 5, 3, 100, 2, 10 ,6]

def test_traverse3(tree3):
    assert tree3.Pre_order_rec() ==  [29, 53, 33, 1, 2, 49 ,68]

# def test_traverse4(tree4):
#     try:
#         tree4.Pre_order_rec() 
#     except Exception as exs:
#         assert ' ' ,  tree4.Pre_order_rec() 

def test_converter(tree1):
    assert converter(tree1) == {1: 411, 2: 294, 4: 60, 7: 733, 5: 967, 3: 177, 6: 850}

def test_converter2(tree2):
    assert converter(tree2) == {8: 616, 5: 967, 3: 177, 100: 443, 2: 294, 10: 939, 6: 850}

def test_converter3(tree3):
    assert converter(tree3) == {29: 793, 53: 120, 33: 354, 1: 411, 2: 294, 49: 559, 68: 442}


def test_tree_intersection1(tree1 , tree2):
    assert tree_intersection(tree1 , tree2) == [2, 5, 3, 6]

def test_tree_intersection2(tree1 , tree3):
    assert tree_intersection(tree1 , tree3) == [1, 2]

def test_tree_intersection3(tree2 , tree3):
    assert tree_intersection(tree2 , tree3) == [2]