# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # my solution
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        flat_list = []
        
        current = head
        
        while current:
            flat_list.append(current)
            current = current.next
        
        removeIdx = len(flat_list) - n
        
        if removeIdx == 0:
            return head.next
        
        flat_list[removeIdx - 1].next = flat_list[removeIdx].next
        
        return head
    
    # two pointer solution (O(1) space complexity)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        
        for i in range(n):
            if not r.next:
                return head.next
            
            r = r.next
        
        while r.next:
            l, r = l.next, r.next
        
        l.next = l.next.next
        
        return head