class Node:
  def __init__(self, data=None, next=None):
    self.data = data #integers, numbers and etc.
    self.next = next #pointer to the next element

class LinkedList:
  def __init__(self):
    self.head = None #head of the ll
 
  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def print(self):
    if self.head is None:
      print("ll is empty")
      return
    res = []
    itr = self.head
    while itr:
      res.append(str(itr.data))
      itr = itr.next 
    print("-->".join(res) + " -> None")
      

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    itr = self.head
    while itr.next:
      itr = itr.next

    itr.next = Node(data, None)
if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_beginning(n1)
  ll.insert_at_beginning(n2)
  ll.print()
