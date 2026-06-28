# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        
        if length - n == 0:
            return head.next
        elif not head:
            return None
        
        current = previous = head
        for i in range(length-n):
            previous = current
            current = current.next

        previous.next = current.next if current else None

        return head
