# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head:
            fast = head.next
        else:
            return False
        while fast:
            # if slow and hast pointers equal each other
            if fast == slow:
                return True

            # move pointers along
            slow = slow.next
            if fast.next == None or fast.next.next == None:
                return False
            fast = fast.next.next

        return False
