class Solution:
    def rob(self, nums: List[int]) -> int:        
        step_2 = 0
        step_1 = 0

        for num in nums:
            current = max(step_1, num + step_2)
            step_2 = step_1
            step_1 = current
        
        return step_1