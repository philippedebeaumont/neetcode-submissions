from math import ceil
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[r]<nums[l] and r-l>1:
            middle = ceil(((r-l)/2)+l)
            print(middle)
            if nums[middle] > nums[l]:
                l = middle
            else:
                r = middle
            print(nums[l], nums[r])
        return min(nums[l], nums[r])

