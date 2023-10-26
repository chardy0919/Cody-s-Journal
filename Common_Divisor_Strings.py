# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        length1 = len(str1)
        length2 = len(str2)
        if length1 >= length2:
            bigger = str1
            smaller = str2
        elif length1 < length2:
            bigger = str1
            smaller = str2       
        i = len(smaller)
        while i > 0:
            gcd = smaller[:i]
            # print(len(bigger), len(smaller), len(gcd))
            if gcd * (len(bigger)//(len(gcd))) == bigger and gcd * (len(smaller)//(len(gcd))) == smaller:
                return gcd
            i-=1
        return ""

        
cody = Solution()
print(cody.gcdOfStrings('ABCABC', 'ABC'))
print(cody.gcdOfStrings('ABABAB', 'ABAB'))
print(cody.gcdOfStrings('LEET', 'CODE'))

# Runtime
# Details
# 16ms
# Beats 56.48%of users with Python
# Memory
# Details
# 13.54MB
# Beats 15.15%of users with Python