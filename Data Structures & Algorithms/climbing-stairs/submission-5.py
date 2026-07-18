class Solution:
    def climbStairs(self, n: int) -> int:
        current, previous = 1, 1

        for i in range(2, n+1):
            tmp = current
            current = current + previous
            previous = tmp
        
        return current
