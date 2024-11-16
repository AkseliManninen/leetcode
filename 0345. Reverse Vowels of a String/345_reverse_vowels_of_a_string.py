# Time comlexity: O(n)
# Spece complexity: O(n)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ["a", "e", "i", "o", "u"]
        
        s_vowels = [c for c in s if c.lower() in vowels]

        res = ""
        for i in range(len(s)):
            if s[i].lower() not in vowels:
                res += s[i]
            else:
                res += s_vowels[-1]
                s_vowels = s_vowels[:-1]
        
        return res