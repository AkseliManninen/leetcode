# Runtime 483 ms

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        num_counts = {}
        count = 0

        for num in nums:
            complement = k - num
            if complement in num_counts:
                count += 1
                num_counts[complement] -= 1
                if num_counts[complement] == 0:
                    del num_counts[complement]
            else:
                if num in num_counts:
                    num_counts[num] += 1
                else:
                    num_counts[num] = 1
        return count