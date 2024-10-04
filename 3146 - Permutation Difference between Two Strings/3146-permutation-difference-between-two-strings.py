# Runtime 18 ms

class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        sum = 0
        for i, c in enumerate(s):
            sum += abs(i - t.index(c))

        return sum

        