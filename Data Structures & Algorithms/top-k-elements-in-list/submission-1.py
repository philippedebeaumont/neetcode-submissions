from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        arr = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            arr[cnt].append(num)
        
        res = []
        for i in range(len(arr)-1, 0, -1):
            res += arr[i]
            if len(res) == k:
                return res
