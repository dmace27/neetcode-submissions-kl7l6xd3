# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        sz = 0
        temp = head
        while temp != None:
            temp = temp.next
            sz += 1

        if sz == n:
            return head.next

        current = ListNode()
        current.next = head
        trailing = ListNode()
        trailing.next = dummy
        for i in range(sz-n+1):
            trailing = trailing.next
            current = current.next
        
        trailing.next = current.next
        
        return head