# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        arr = []
        def fn( root , s ):
            if not root:
                return s
            s += str(root.val)
            if not root.left and not root.right:
                arr.append(s)
                s = s[:-1]
                return s
            s = fn(root.left,s)
            s = fn(root.right,s)
            s = s[:-1]
            return s
        s = fn(root,"")
        print(s,arr)
        # all good above this

        final = 0
        for i in arr:
            temp = 0
            k = 0
            for j in i[::-1]:
                temp += int(j)*(2**k) 
                k+=1
            final += temp
            print(final)
        return final