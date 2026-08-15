class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        
        max_area = 0
        while left < right:
            lh = heights[left]
            rh = heights[right]
            area = (right-left)*min(lh, rh)
            
            if area > max_area:
                max_area = area
            
            if lh > rh:
                right -=1
            else:
                left+=1

        return max_area
            


        