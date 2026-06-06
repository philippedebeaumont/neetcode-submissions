class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in numset:
                i = 1
                while num + i in numset:
                    i += 1
                if i >= res:
                    res = i
        return res
                