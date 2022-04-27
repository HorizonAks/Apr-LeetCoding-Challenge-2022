#Day 25
#284. Peeking Iterator

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cache = iterator
        self.mem = []
        while(self.cache.hasNext()):
            self.mem.append(self.cache.next())
        self.ptr = -1
        #print(self.mem)
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext(): return self.mem[self.ptr+1]

    def next(self):
        """
        :rtype: int
        """
        self.ptr+=1
        return self.mem[self.ptr]

    def hasNext(self):
        """
        :rtype: bool
        """
        #print(self.ptr)
        return self.ptr < len(self.mem)-1
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
