# Runtime 19 ms

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while True:
            num = low + (high-low) // 2
            ans = guess(num)
            if ans == 1:
                low = num+1
            elif ans == -1:
                high = num-1
            else:
                return num