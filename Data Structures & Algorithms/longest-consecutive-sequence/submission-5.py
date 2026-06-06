from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        res = 0

        for num in nums:
            if not hashmap[num]:
                hashmap[num] = hashmap[num-1] + hashmap[num+1] + 1
                hashmap[num - hashmap[num-1]] = hashmap[num]
                hashmap[num + hashmap[num+1]] = hashmap[num]
                res = max(res, hashmap[num])
        
        return res
        