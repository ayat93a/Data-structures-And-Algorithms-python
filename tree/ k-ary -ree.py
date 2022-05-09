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