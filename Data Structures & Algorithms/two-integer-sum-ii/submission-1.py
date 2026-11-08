class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            left = i+1 
            right = len(numbers) - 1 
            ans = self.binarysearch(numbers ,left ,right , compliment)
            if ans != -1 :
                print(ans)
                return [i+1 , ans+ 1] 
    def binarysearch(self,arr , left, right , target ):
        while left <= right :
            mid = (left + right ) // 2 
            if arr[mid] == target :
                return mid 
            elif arr[mid] > target :
                right = mid -1 
            else :
                left = mid + 1
        return -1
        