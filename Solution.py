"""
// Time Complexity :O(log N)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode :yes
// Any problem you faced while coding this :
   how to use a boolean part took time
   figuring out the edge case took time while submiting in the leet code [2,2], target =2


// Your code here along with comments explaining your approach

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
 
        low=0
        high=(len(nums))-1
        found=False
        while(low<=high):
            mid=low+(high-low)//2
            #instead of returning the index while finding the element in mid, set a bool variable to True 
            if nums[mid]==target:
                found=True
                break
            
            elif(nums[mid]>target):
                high=mid-1
            
            else:
                low=mid+1
        #when found one target in nums , start searching having low pointer mid-1 moving leftwards and high pointer moving rightwards and look for target
        if found:
            low=mid-1
            high=mid+1
            
            
            while low>=0 and nums[low]==target:
                low-=1
            while high<=len(nums)-1 and nums[high]==target:
                high+=1
            
            return [low + 1, high- 1]
            
        return[-1,-1]