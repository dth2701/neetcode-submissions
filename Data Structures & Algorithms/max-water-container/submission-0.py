class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # using 2 pointer strategy
        # Having maxArea to save the maximum area
        # area = minHeght * distance 
        # Get the minHeight between the current i-th index height and the height at the pointer
        # Only move pointer if that number is smaller
        # Calculate the currArea to compare with Maximum area

        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, min(heights[l], heights[r]) * (r-l) )
            if heights[l] < heights[r]: 
                l += 1
            else:
                r -= 1
        return maxArea
            
