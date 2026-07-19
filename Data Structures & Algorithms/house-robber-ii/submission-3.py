class Solution:
    def rob(self, nums: List[int]) -> int:       
        def rob_linear(houses):
            step_1, step_2 = 0, 0

            for money in houses:
                step_2, step_1 = step_1, max(step_1, step_2 + money)
            
            return step_1

        ignore_first = rob_linear(nums[1:])
        ignore_last = rob_linear(nums[:-1])

        return max(nums[0], ignore_first, ignore_last)
