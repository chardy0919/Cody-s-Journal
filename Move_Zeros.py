# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # non_zero_elements = []
        # count = 0 '
        # for num in nums:
        #     if num != 0:
        #         non_zero_elements.append(num)
        #     else:
        #         count += 1
        # while count > 0:
        #     non_zero_elements.insert(len(non_zero_elements),0)
        #     count-=1
        # return non_zero_elements
        
        zero_count = nums.count(0)  # Count the number of zeros in the list
        non_zero_elements = [num for num in nums if num != 0]  # Collect non-zero elements
        non_zero_elements.extend([0] * zero_count)  # Append the necessary number of zeroes to the end
        print(non_zero_elements)
        nums[:] = non_zero_elements 
        return nums
cody = Solution()
print(cody.moveZeroes([0,1,0,3,12])) #[1,3,12,0,0]

