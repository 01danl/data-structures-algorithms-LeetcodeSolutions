class ListNode():
    def __init__(self, val):
        self.val = val 
        self.next = None 

def merge_sort(head):
    if head is None or not head.next:
        return head

    slow, fast = head, head.next # slow (0) fast (1)

    while fast and fast.next: #divide
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)

    dummy = ListNode()
    curr = dummy

    while left and right:
        if left.val < right.val:
            curr.next = left #create value new nodes - > - >
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next 
    
    curr.next = left or right 
    return dummy.next 


