# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        l = None
        if curr1 and curr2:
            if curr1.val > curr2.val:
                l = curr2
                curr2 = curr2.next
            else:
                l = curr1
                curr1 = curr1.next
        elif curr1:
            l = curr1
            curr1 = curr1.next
        elif curr2:
            l = curr2
            curr2 = curr2.next
        else:
            return l
        head = l
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val > curr2.val:
                    l.next = curr2
                    curr2 = curr2.next
                else:
                    l.next = curr1
                    curr1 = curr1.next
                l = l.next
            elif not curr2:
                l.next = curr1
                l = l.next
                curr1 = curr1.next
            else:
                l.next = curr2
                l = l.next
                curr2 = curr2.next
    
        
        return head
            