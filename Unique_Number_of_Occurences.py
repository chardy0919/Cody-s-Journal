class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for num in arr:
            if num in dict:
                dict[num] = dict[num] + 1
            else:
                dict[num] = 1
        occurs = dict.values()
        occurs_occurs = {}
        for num in occurs:
            if num in occurs_occurs:
                return False
            else:
                occurs_occurs[num] = 1
        return True
        

cody = Solution()
print(cody.uniqueOccurrences([1,2,2,1,1,3]))
print(cody.uniqueOccurrences([1,2,1,1,3]))

# Runtime
# Details
# 24ms
# Beats 28.54%of users with Python
# Memory
# Details
# 13.20MB
# Beats 78.25%of users with Python