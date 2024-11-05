# Time complexity: O(n)
# Memory complexity: O(1)

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        dict1 = {}
        dict2 = {}
        for i in range(len(word1)):
            if word1[i] in dict1.keys():
                dict1[word1[i]] += 1
            else:
                dict1[word1[i]] = 1
            if word2[i] in dict2.keys():
                dict2[word2[i]] += 1
            else:
                dict2[word2[i]] = 1
        
        return sorted(list(dict1.values())) == sorted(list(dict2.values()))


        