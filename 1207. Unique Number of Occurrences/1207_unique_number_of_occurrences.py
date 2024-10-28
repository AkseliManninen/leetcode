# Runtime 0 ms, beats 100%

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurences = {}
        for num in arr:
            occurences[str(num)] = occurences.get(str(num), 0) + 1
        
        return len(set(occurences.values())) == len(occurences)
