class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def Search(head,key):
  curr = head
  #curr.data = data, curr = link
  while curr is not None:
    if curr.data == key:
      return True

    curr = curr.next
  return False

def main():
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)
  head.next.next.next = Node(40)
  key = 20

  print(Search(head, key))

if __name__ == "__main__":
  main()
