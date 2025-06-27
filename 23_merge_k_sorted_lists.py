from typing import Optional, List
import heapq

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        heap = []
        
        for list in lists:
            while list:
                heapq.heappush(heap, (list.val, list))
                list = list.next
        
        for i in range(len(heap) - 1):
            heap[i][1].next = heap[i + 1][1]
        
        
        return heap[0][1]
        
        