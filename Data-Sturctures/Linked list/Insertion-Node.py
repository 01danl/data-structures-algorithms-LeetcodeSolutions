class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def insertion(head, position, value):
  if position < 1:
    return "You enter a wrong position"

  if position == 1:
    newNode = Node(value)
    newNode.next = head
    return newNode

  curr = head

def print(head):
  curr = head
  while curr is not None:
    print(curr, end = " ")
    curr.next

    
  
