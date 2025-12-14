#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a_sum = (n*(n+1))//2
        sum = 0
        for i in range(n):
            sum += nums[i]
        return a_sum - sum
