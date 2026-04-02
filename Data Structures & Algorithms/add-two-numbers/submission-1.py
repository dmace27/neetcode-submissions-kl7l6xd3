# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        ptr = l1
        carry = 0
        while ptr != None:
            ptr = ptr.next
            n += 1
        
        dummy1 = ListNode()
        d1 = dummy1 
        while l1 or l2 or carry:
            v1= l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            d1.next = ListNode(val)
            d1 = d1.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy1.next
            
