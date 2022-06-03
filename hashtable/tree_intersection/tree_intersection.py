from hashtable.hashtable import Hashtable

hash = Hashtable()
class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
  
class BinaryTree(TNode):
    def __init__(self):
        self.root = None

    def Pre_order_rec(self):
        my_list= []
        def _traverse(node):

            if self.root == None:
                raise Exception ('This is an empty tree ! nothing to traverse ')

            if node:
                my_list.append(node.value)
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)

        _traverse(self.root)
        return my_list

def converter(tree):
    tree_traverse = tree.Pre_order_rec()
    _hash = Hashtable()
    dic ={}
    for i in tree_traverse:
        dic.update({ i: _hash.hash(i) })
    return dic

def tree_intersection(tree1 , tree2):
    lst = []
    tree1_converted=converter(tree1)
    tree2_converted=converter(tree2)
    for i,j in tree1_converted.items():
        for x,y in tree2_converted.items():
            if i == x :
                lst.append(i)
    return lst





if __name__ == '__main__':
    tree1= BinaryTree ()

    node1 = TNode(7)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5 = TNode(5)
    node6=TNode(6)
    node7 = TNode(100)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    node4.left = node7
    tree1.root = node1
    # print(tree1.Pre_order_rec())
    


    tree2 =BinaryTree()
    node10 = TNode(7)
    tree2.root = node10 
    node20= TNode(21)
    node30 = TNode(13)
    node40 = TNode(4)
    node50 = TNode(25)
    node60=TNode(6)
    node70 = TNode(100)


    node10.left = node20
    node10.right = node30
    node20.left = node40
    node20.right= node50
    node30.left= node60
    node40.left = node70
    # print(tree2.Pre_order_rec())

    # print(value(tree1 , tree2))
    print(converter(tree1))
    print(tree_intersection(tree1,tree2))

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

    print(converter(tree3))
