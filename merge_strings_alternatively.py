# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer = ""
        idx = 0
        while len(answer)<len(word1)+len(word2):
            if idx < len(word1):
                answer = answer + word1[idx]
            if idx < len(word2):    
                answer = answer + word2[idx]
            idx+=1
        return answer

cody = Solution()
print(cody.mergeAlternately('abc', 'pqr'))
print(cody.mergeAlternately('ab', 'pqrs'))

# Runtime 14ms
# Beats 63.30%of users with Python
# Memory 13.29MB
# Beats 63.42%of users with Python
        