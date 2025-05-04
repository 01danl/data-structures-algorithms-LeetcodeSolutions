class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

def traverse(head):
  curr = head
  while curr is not None:
    print(curr.data, end = " ")
    curr = curr.next

def main():
  head = Node(1)
  second = Node(2)
  third = Node(3)

  head.next = second
  second.prev = head
  second.next = third
  third.prev = second

  traverse(head)
if __name__ == "__main__":
  main()
