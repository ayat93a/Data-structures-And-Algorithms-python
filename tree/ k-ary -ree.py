"""The parent node. So you can come back to the parent if you are finished.
The current child node so you know which one to take next.

For each node, you handle all the kids.
If a kid is handled, you check if there is a next kid and handle that (updating the current).
If all kids are handled, go back to the parent.
If the node is NULL, quit."""

"""
ALGORITHM breadthFirst(root)
// INPUT  <-- root node
// OUTPUT <-- front node of queue to console

  Queue breadth <-- new Queue()
  breadth.enqueue(root)

  while ! breadth.is_empty()
    node front = breadth.dequeue()
    OUTPUT <-- front.value

    for child in front.children
        breadth.enqueue(child)
"""

from queue import deque
class Node:
   def __init__(self, value, child = None) -> None:
      self.val = value
      self.children = []
      if child != None:
         for value in child:
            self.children.append(value)

def solve(root):
   if not root:
      return root
   head = Node(root.val)
   q = deque([(root, head)])
   while q:
      node, cloned = q.popleft()
      for chld in node.children:
         new_n = Node(chld.val)
         cloned.children.append(new_n)
         q.append((chld,new_n))
   return head

def treeprint(node, tree):
   if node == None:
      tree.append("None")
      return tree
   if tree == None:
      tree = []
   tree.append(node.val)
   for child in node.children:
      treeprint(child, tree)
   return tree

node6 = Node(65)
node5 = Node(56)
node4 = Node(42, [node5, node6])
node3 = Node(32)
node2 = Node(27)
node1 = Node(14, [node2, node3, node4])
root = node1

copynode = solve(root)
print(treeprint(copynode, None))