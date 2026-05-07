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
        if not head:
            return None

        # Dictionary to map: Original Node -> New Copied Node
        # We pre-fill None: None to handle pointers that point to null
        old_to_new = {None: None}

        # First Pass: Create all nodes and store them in the map
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second Pass: Connect the 'next' and 'random' pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            # Use the map to find the copy of the next/random nodes
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]