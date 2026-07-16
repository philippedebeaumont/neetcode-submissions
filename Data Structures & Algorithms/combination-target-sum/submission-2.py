class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def backtracking(current_path, start_index, current_sum):
            if current_sum == target:
                res.append(current_path.copy())
                return
            
            for i in range(start_index, len(nums)):
                if current_sum + nums[i] > target:
                    continue
                current_path.append(nums[i])

                backtracking(current_path, i, current_sum + nums[i])
                current_path.pop()
        
        backtracking([], 0, 0)

        return res