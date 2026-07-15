class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def backtracking(current_path, start_index, current_sum):
            if current_sum == target:
                res.append(current_path.copy())
                return
            
            for i in range(start_index, len(nums)):
                n = nums[i]
                if current_sum + n > target:
                    continue
                current_path.append(n)
                current_sum += n

                backtracking(current_path, i, current_sum)

                current_path.pop()
                current_sum -= n
        
        backtracking([], 0, 0)

        return res