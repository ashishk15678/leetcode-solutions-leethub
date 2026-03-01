class Solution:
    def minPartitions(self, n: str) -> int:
        m = -1
        for i in n:
            l = int(i)
            if l > m:
                m = l
        return m