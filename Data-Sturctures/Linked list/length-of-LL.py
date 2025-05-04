class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def FindTheLength(head):
  curr = head
  count = 0
  
  while curr is not None:
    count += 1
    curr = curr.next   
  return count

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  print(FindTheLength(head))
  
if __name__ == "__main__":
  main()
