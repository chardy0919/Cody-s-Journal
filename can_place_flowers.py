# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for idx in range(len(flowerbed)-1):
            if idx == 0 and flowerbed[idx] == 0 and flowerbed[idx+1] == 0:
                n-=1
            elif idx == len(flowerbed-1 ) and flowerbed[idx] == 0 and flowerbed[idx+1] == 0:
                n-=1
            elif flowerbed[idx] == 0 and flowerbed[idx+1] == 0 and flowerbed[idx-1] == 0:
                n-=1

        for i in range(len(flowerbed)-1):
            print(f"i={i}")
            for j in range(len(flowerbed[i:])):
                print(f"i={flowerbed[i]}, j={flowerbed[j]}")
                


cody = Solution()
print(cody.canPlaceFlowers([1,0,0,0,1], 1))