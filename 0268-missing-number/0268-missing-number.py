class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+2):
            if i not in nums:
                return i