# Runtime 8 ms

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        res = ""
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            res += word1[i] + word2[i]
        
        return res + word1[min_len:] + word2[min_len:]