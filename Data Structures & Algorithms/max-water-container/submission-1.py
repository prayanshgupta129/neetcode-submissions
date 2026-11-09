class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left = 0 
        right = len(heights)-1
        width = right - left 
        while left < right :
            length = min(heights[left],heights[right])
            area = width * length
            maxarea = max(area,maxarea)
            width -= 1
            if heights[left] >= heights[right]:
                right = right - 1
            else :
                left = left + 1

        
        return maxarea
                
                    

        