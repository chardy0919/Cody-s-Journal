# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def searchInsert(self, nums, target):
        left = nums[0]
        right = len(nums)
        while left < right:
            middle = (right + left)//2
            if target < nums[middle]:
                right = middle
            elif target > nums[middle]:
                left = middle+1
            else:
                return middle
        return left
    