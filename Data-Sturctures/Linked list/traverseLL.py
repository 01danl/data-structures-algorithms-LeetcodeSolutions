"""
Traversal of Singly Linked List

Traversal of Singly Linked List is one of the fundamental operations, where we traverse or visit each node of the linked list. 
In this article, we will cover how to traverse all the nodes of a singly linked list along with its implementation.

"""

class Node:
  def __init__(self, data): #initialize new node
    self.data = data
    self.next = None

def Traverse(head):

  while head is not None:
    print(head.data, end = " ")
    head = head.next

def main():
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)
  head.next.next.next = Node(40)
  head.next.next.next.next = Node(50)

  Traverse(head)

if __name__ == "__main__":
  main()
