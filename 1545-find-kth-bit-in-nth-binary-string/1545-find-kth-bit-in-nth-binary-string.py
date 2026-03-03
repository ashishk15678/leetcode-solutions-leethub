class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s:str):
            n = ""
            for i in s:
                if i == "0":
                    n += "1"
                else:
                    n += "0"
            return n
        
        start = "0"
        # simulating the process , but for n times
        for i in range(1,n):
            start = start + "1" + invert(start[::-1])
        print(f"start = {start}")
        return start[k-1]

        