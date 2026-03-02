class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        swaps = 0
        
        for i in range(N):
            required_zeros = N - 1 - i
            
            found_idx = -1
            for j in range(i, N):
                count = 0
                for k in range(N - 1, -1, -1):
                    if grid[j][k] == 0:
                        count += 1
                    else:
                        break
                
                if count >= required_zeros:
                    found_idx = j
                    break
            
            if found_idx == -1:
                return -1
            
            swaps += (found_idx - i)
            
            row_to_move = grid.pop(found_idx)
            grid.insert(i, row_to_move)

        return swaps