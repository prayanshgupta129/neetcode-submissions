class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        res = 0
        for n in nums :
            if n-1 in nums:
                count = 0 
                continue 
            curr = n+1 
            count += 1
            while curr in nums :
                
                curr = curr + 1
                count += 1
            res = max(res, count)
            count = 0
        return res
            



        