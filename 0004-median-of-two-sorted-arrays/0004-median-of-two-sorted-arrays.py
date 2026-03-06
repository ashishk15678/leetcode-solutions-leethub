class Solution:
    def findMedianSortedArrays(self, nums: List[int], nums2: List[int]) -> float:
        final = nums.extend(nums2)
        nums = sorted(nums)
        return nums[len(nums)//2] if len(nums) % 2 == 1 else (nums[len(nums)//2] + nums[(len(nums)//2 )- 1]) /2  