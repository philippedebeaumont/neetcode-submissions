# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, previous = head, None
        while current:
            node = ListNode(current.val, previous)
            previous = node
            current = current.next
        return previous
