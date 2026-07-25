class Solution:
    def canJump(self, nums: List[int]) -> bool:
        counter = 0

        for i in range(1, len(nums)):
            counter = max(counter, nums[i-1])

            if counter == 0:
                return False
            
            counter -= 1
        
        return True
