"""
class Node:
  def __init__(self, val):
    self.head = head
    self.next = None
"""
#Using Dummy in the interviews is the common method in solution of exercises(LL)

#without Dummy
def add(l1 : ListNode):
  if not l1:
    return None

  newHEAD = ListNode(l1.val * 2)
  cur = newHEAD
  l1 = l1.next

  while l1 is not None:
    cur.next = ListNode(v1.val * 2)
    cur = cur.next
    l1 = l1.next
  return newHEAD


  
def add_w_dummy():
  dummy = ListNode() #new list node
  cur = dummy

  while l1:
    cur.next = ListNode(l1.val * 2)
    cur = cur.next
    l1 = l1.next
  return dummy.next #return new head
