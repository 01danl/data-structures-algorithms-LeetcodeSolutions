class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class List:
  def __init__(self, items=None):
    if items == None:
      items = []
    self.head: Node = Node(None)
    self.tail: Node = Node(None)
    self.head.next = self.tail
    self.tail.prev = self.head

    for item in items:
      self.push_back(item)

  def push_front(self, data : Any) -> None: #adding to the (head - tail)
    node = Node(data)
    node.prev = self.head
    self.head.next.prev = node #old head.next after head: initialize to new
    self.head.next = node
  def push_back(self, data : Any) -> None:
    node = Node(data)
    node.prev = self.tail.prev
    node.next = self.tail
    self.tail.prev.next = node # old tail.prev before tail 
    self.tail.prev = node # initialize new var
    
