class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        withoutzeroproduct = 1
        zerocount = 0
        for i in range(len(nums)) :
            if nums[i] == 0 :
                zerocount += 1
                if zerocount >= 2 :
                    return [0] * len(nums)
            if nums[i] != 0 :
               withoutzeroproduct *= nums[i]
            product = product * nums[i]
        res = []
        for i in range(len(nums)):
            if product == 0 :
                if nums[i] != 0 :
                    res.append(0)
                else :
                    res.append(withoutzeroproduct)

            else :
                res.append( product // nums[i])
        return res 