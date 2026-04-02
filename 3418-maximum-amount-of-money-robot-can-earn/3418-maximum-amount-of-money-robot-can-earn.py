class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-math.inf] * 3 for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0 # Neutralize the very first cell
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                val = coins[i][j]
                
                for k in range(3):
                    best_prev = -math.inf
                    if i > 0:
                        best_prev = max(best_prev, dp[i-1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j-1][k])
                        
                    # Option A: Don't use the ability on the current cell
                    if best_prev != -math.inf:
                        dp[i][j][k] = max(dp[i][j][k], best_prev + val)
                        
                    # Option B: Use the ability on the current cell (Only if it's a robber and we have allowed uses)
                    if val < 0 and k > 0:
                        best_prev_k_minus_1 = -math.inf
                        if i > 0:
                            best_prev_k_minus_1 = max(best_prev_k_minus_1, dp[i-1][j][k-1])
                        if j > 0:
                            best_prev_k_minus_1 = max(best_prev_k_minus_1, dp[i][j-1][k-1])
                            
                        # If we used k-1 abilities previously, we use the k-th ability here (adding 0 instead of val)
                        if best_prev_k_minus_1 != -math.inf:
                            dp[i][j][k] = max(dp[i][j][k], best_prev_k_minus_1)
                            
        
        return max(dp[m-1][n-1])