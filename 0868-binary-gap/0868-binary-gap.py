class Solution:
    def binaryGap(self, n: int) -> int:
        last_seen = -1
        max_gap = 0
        i = 0
        
        while n > 0:
            if n % 2 == 1:
                if last_seen != -1:
                    max_gap = max(max_gap, i - last_seen)
                last_seen = i            
            n //= 2
            i += 1
        return max_gap