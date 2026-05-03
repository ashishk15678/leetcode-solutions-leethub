class Solution:
    def rotateString(self,s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
    
        for i in range(len(goal)):
            # If we find a character matching the start of s
            if goal[i] == s[0]:
                # Rearrange goal to see if it matches s
                # We slice goal from the index to the end, then add the start
                temp = goal[i:] + goal[:i]
                if temp == s:
                    return True
                    
        return False
    