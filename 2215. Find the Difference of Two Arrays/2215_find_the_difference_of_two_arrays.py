# Runtime 1 ms

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]
