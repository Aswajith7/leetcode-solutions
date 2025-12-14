#Given an integer array nums, find the subarray with the largest sum, and return its sum.



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i_sum=nums[0]
        max_sum=nums[0]
        for i in range (1,len(nums)):
            i_sum = max(i_sum+nums[i],nums[i])
            max_sum = max(max_sum,i_sum) 
        return max_sum

                
