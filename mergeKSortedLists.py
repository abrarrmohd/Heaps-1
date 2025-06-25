"""
Problem: mergeKLists
Approach: put the linked list in the heap and get the min head each time and add it to the reference list.
t.c. => N=number of nodes in total, k= len(lists), O(Nlogk)
s.c. => O(k)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(minHeap, [lists[i].val, i])
            
        prevNode = ListNode()
        head = prevNode

        while minHeap:
            val, idx = heapq.heappop(minHeap)
            pop = lists[idx]
            head.next = pop
            pop = pop.next
            head.next.next = None
            if pop:
                heapq.heappush(minHeap, [pop.val, idx])
                lists[idx] = pop
            head = head.next
        return prevNode.next

