#Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        rev = nums.sort(reverse = True)
        l = len (nums)
        if l > 2 :
            return nums[2]
        else :
            return nums[0]
        
