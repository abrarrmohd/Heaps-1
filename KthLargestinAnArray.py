"""
Problem: findKthLargest
Approach: put the elements to a minHeap of size k and at the end the minHeap top will contain the kth largest 
t.c. => O(nlogk)
s.c. => O(k)
"""
from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        n = len(nums)
        for i in range(n):
            heappush(minHeap, nums[i])
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]