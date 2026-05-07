"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        p = head
        if not head:
            return head
        new_head = Node(head.val)
        np = new_head

        addresses = {}

        # first iteration - creating copy of list without random ptr
        while p.next:
            new_node = Node(p.next.val)
            np.next = new_node
            
            if p.random:
                addresses[p] = p.random
                
            np = np.next
            p = p.next

        if p.random:
            addresses[p] = p.random
        
        # second iteration - adding random pointers based on dict
        np = new_head
        p = head
        while np:
            
            # iterate throught to get to correct node
            if p in addresses:
                s = head
                sn = new_head
                while s != addresses[p]:
                    s = s.next
                    sn = sn.next
                
                np.random = sn

            np = np.next
            p = p.next
        
        return new_head

        