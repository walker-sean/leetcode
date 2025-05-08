# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        second_half = slow.next
        slow.next = None
        node = None
        
        while second_half:
            temp = second_half.next
            second_half.next = node
            node = second_half
            second_half = temp
        
        
        first_half = head
        second_half = node
        
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next, second_half.next = second_half, temp1
            first_half, second_half = temp1, temp2
        
        
