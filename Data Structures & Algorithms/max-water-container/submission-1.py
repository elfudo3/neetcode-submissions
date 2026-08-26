class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curr_largest = 0

        while l < r:
            
            area = min(heights[l], heights[r]) * (r - l)

            if area > curr_largest:
                curr_largest = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return curr_largest
            
            