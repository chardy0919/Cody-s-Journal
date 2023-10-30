# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        most = max(candies) 
        answer = []
        for num in candies:
            answer.append((num+extraCandies)>= most)
        return answer
cody = Solution()
print(cody.kidsWithCandies([2,3,5,1,3],3))

# Runtime
# Details
# 22ms
# Beats 42.67%of users with Python
# Memory
# Details
# 13.28MB
# Beats 35.96%of users with Python
# First Try!