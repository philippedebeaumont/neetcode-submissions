class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        if self.head is None:
            return -1
        for _ in range(index):
            if current.next == None:
                return -1
            current = current.next
        return current.val

    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head
        self.head = new

    def insertTail(self, val: int) -> None:
        new = ListNode(val)
        current = self.head
        if self.head is None:
            self.head = new
            return
        while current.next:
            current = current.next
        current.next = new  

    def remove(self, index: int) -> bool:
        current = self.head
        if self.head is None:
            return False
        elif index == 0:
            self.head = self.head.next
            return True
        for _ in range(index-1):
            if current.next is None:
                return False
            current = current.next
        if current.next is None:
            return False
        current.next = current.next.next
        return True

    def getValues(self) -> List[int]:
        values, current = [], self.head
        while current:
            values.append(current.val)
            current = current.next
        return values
