class ListNode:
  def __init__(self, data):
    self.data = data
    self.next = None
#last.next -> head in regular LL
def InsertValueBeg(last, VALUE):
  new_node = ListNode(VALUE)

  new_node.next = last.next
  last.next = new_node

  return last

def printLL(last):
  head = last.next

  while True:
    print(head.data, end = " ")
    head = head.next
    if head == last.next:
      break
  
def main():
  first = ListNode(1)
  first.next = ListNode(2)
  first.next.next = ListNode(3)
  last = first.next.next
  last.next = first

  VALUE2 = 10
  print(InsertValueBeg(last, VALUE2))
  printLL(last)
  
if __name__ == "__main__":
  main()
