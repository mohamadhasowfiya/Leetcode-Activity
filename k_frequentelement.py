class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        heap=[]
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
