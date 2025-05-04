class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

def InsertionDLL(head, value):
  curr = head
  SecondNode = Node(value)
  SecondNode.next = curr

  if curr is not None:
    curr.prev = SecondNode
  return SecondNode

def printLL(head):
  curr = head
  while curr is not None:
    print(curr.data, end = " ")
    curr = curr.next
    
def main():
  head = Node(1)
  head.next = Node(2)
  head.next.prev = head
  head.next.next = Node(3)
  head.next.next.prev = head.next
  head.next.next.next = Node(4)
  head.next.next.next.prev = head.next.next

  value = 4
  head = InsertionDLL(head, value)
  printLL(head)
if __name__ == "__main__":
  main()
