#Day 8.
#703. Kth Largest Element in a Stream

"""
Solution Explanation:
Inputs:
arr=[4,5,8,2]
k=3
now we are going to make heap
heap=[2,4,5,8]
now we are going to pop the element which is 2 and make our heap=[4,5,8] because we need only k sized heap
Big o:
n-->size of the s
Time: O((n-k)log n) k could be small so O(n logn)
Space: O(n)

Code:
"""
import heapq

class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        print(f'Heap : {self.minHeap}')
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) # it will remove the smallest element from the heap 


    def add(self, val) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
