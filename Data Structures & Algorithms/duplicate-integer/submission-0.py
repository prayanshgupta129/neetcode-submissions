from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums) -> bool:
        freq_map = defaultdict(int)
        for i in range(len(nums)):
            freq_map[nums[i]] += 1
            if freq_map[nums[i]] > 1 :
                return True
        return False
        