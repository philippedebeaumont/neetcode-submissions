# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find length
        current = head
        length = 0
        while current.next:
            current = current.next
            length += 1
        
        # Split into two halves
        current = head
        current_length = 0
        while current_length < length // 2:
            current = current.next
            current_length += 1
        
        head2 = current.next
        current.next = None
        
        # Reverse second linked list
        current = head2
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        # Merge two lists
        current = head
        current2 = previous
        while current2:
            tmp1, tmp2 = current.next, current2.next
            current.next = current2
            current2.next = tmp1
            current, current2 = tmp1, tmp2
