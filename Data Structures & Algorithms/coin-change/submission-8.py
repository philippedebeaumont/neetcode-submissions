class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = float("inf")
        coins.sort(reverse=True)

        def dfs(start_idx, current_sum, current_count):
            nonlocal min_coins
            if current_sum == amount:
                min_coins = min(min_coins, current_count)
            
            for i in range(start_idx, len(coins)):
                if current_sum + coins[i] > amount:
                    continue
                if current_count > min_coins:
                    break
                
                dfs(i, current_sum + coins[i], current_count + 1)


        dfs(0, 0, 0)
        return min_coins if min_coins != float("inf") else -1