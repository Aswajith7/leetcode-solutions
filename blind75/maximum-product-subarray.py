#Given an integer array nums, find a subarray that has the largest product, and return the product.

#The test cases are generated so that the answer will fit in a 32-bit integer.

#Note that the product of an array with a single element is the value of that element.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmax,curmin = 1,1
        for n in nums :
            temp = curmax * n
            curmax = max(curmax * n, curmin * n, n)
            curmin = min(temp, curmin * n, n)
            res = max(res,curmax)
        return res
