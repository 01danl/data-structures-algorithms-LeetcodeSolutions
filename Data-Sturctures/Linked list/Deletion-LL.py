class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def DeletionLL(head):
  temp = head
  head = head.next
  del temp
  return head
  
def printLL(head):
  curr = head

  while curr is not None:
    print(curr.data, end= " ")
    curr = curr.next

def main():
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)
  head.next.next.next = Node(40)
  head = DeletionLL(head)
  printLL(head)

if __name__ == "__main__":
  main()
