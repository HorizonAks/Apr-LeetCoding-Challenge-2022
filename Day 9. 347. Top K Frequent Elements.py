#Day 9.
#347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #frequency counter
        counts = dict()

        #count frequency of all elements
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        #sort according to frequency and get a sorted list
        res = sorted(counts.items(), key = lambda x: (x[1],x[0]))
        #return k elements from the back
        return  [res[i][0] for i in range(len(res)-1,len(res)-k-1,-1)]
