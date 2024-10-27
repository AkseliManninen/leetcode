# Runtime 0 ms

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        highest = 0
        current = 0

        for i in gain:
            current += i
            if current > highest:
                highest = current
        
        return highest
