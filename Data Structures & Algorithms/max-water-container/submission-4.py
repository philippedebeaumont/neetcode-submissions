class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_height = 0

        def get_height(l, r):
            return min(heights[l], heights[r]) * (r - l)

        while l < r:
            print(l, r)
            height = get_height(l, r)
            if height > max_height:
                max_height = height
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_height