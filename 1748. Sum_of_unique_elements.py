# Leetcode 1748 - 91% runtime beats, 99% memory beats

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans =0
        set_nums = list(set(nums))
        for i in set_nums:
            if nums.count(i)==1:
                ans+=i
        return ans
