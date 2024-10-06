# Runtime 39 ms

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        counts = {}

        for num in nums:
            if str(num) not in counts.keys():
                counts[str(num)] = 1
            else: 
                ans.append(num)
                if len(ans) == 2:
                    return ans