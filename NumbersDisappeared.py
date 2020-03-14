Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

All testcases passed successfully on Leetcode.
Time Complexity O(n)  
Space Complexity O(1) 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if nums == None or len(nums) == 0:
            return []
        result = []
        #here we are marking the index only to check whether the value is present the array
        #if present we multipy with -1 and before that we need to check if its greater than 0 because repeated number(means already marked values should not be marked again.)
        for i in range(0,len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
#iterate and append the index to the result because we are marking the index values 
        for i in range(0,len(nums)):
            print(nums)
            if nums[i] > 0:
                print(nums[i],i+1)
                result.append(i+1)
        return result
