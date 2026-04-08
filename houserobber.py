class Solution(object):
    def rob(self, nums):
        prev=0
        curr=0
        for num in nums:
            temp = max ( curr,prev+num)
            prev=curr
            curr=temp
        return curr
