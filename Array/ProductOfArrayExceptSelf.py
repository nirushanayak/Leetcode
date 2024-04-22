# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)-1
        result=[1]*(length+1)
        for i in range(1,length+1):
            result[i]=nums[i-1]*result[i-1]
        preEle=nums[length]
        nums[length]=1
        for i in range(length-1,-1,-1):
            curEle=nums[i]
            nums[i]=preEle*nums[i+1]
            preEle=curEle
        for i in range(length+1):
            result[i]=result[i]*nums[i]
        return result


            