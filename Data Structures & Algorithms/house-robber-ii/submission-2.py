class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def rob_linear(houses):
            step_1, step_2 = 0, 0

            for money in houses:
                step_2, step_1 = step_1, max(step_1, step_2 + money)
            
            return step_1

        ignore_first = rob_linear(nums[1:])
        ignore_last = rob_linear(nums[:-1])

        return max(ignore_first, ignore_last)
