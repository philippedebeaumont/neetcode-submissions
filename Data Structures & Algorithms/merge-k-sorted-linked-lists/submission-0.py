# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        merged = lists[0]
        for i in range(1, len(lists)):
            dummy = head =  ListNode(0, None)
            current = lists[i]
            while merged and current:
                if merged.val < current.val:
                    head.next = merged
                    merged = merged.next
                else:
                    head.next = current
                    current = current.next
                head = head.next
            head.next = merged or current
            merged = dummy.next
        return merged