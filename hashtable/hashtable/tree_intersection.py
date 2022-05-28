from hashtable import Hashtable

class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
  
class BinaryTree(TNode ):
    
    def __init__(self):
        self.root = None

    def Pre_order_rec(self):
        hashtable = Hashtable()
        my_list1= []
        my_list2= []
        def _traverse(node1 , node2):

            if self.root == None:
                raise Exception ('This is an empty tree ! nothing to traverse ')

            if node1 and node2:
                # print(node.value)
                my_list1.append(hashtable.get(node1.value))
                my_list2.append(hashtable.get(node2.value))
                if node1.left:
                    _traverse(node1.left)
                if node2.left:
                    _traverse(node2.left)   
                if node1.right:
                    _traverse(node1.right)
                if node2.right:
                    _traverse(node2.right)
                    

        _traverse(self.root)
        return my_list1 , my_list2

def compare(my_list1 , my_list2):
    result =[]
    for i in my_list1:
        for j in my_list2 :
            if i == j:
                result.append(i)
    return result
