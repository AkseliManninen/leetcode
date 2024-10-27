# Runtime 115 ms

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = {"a", "e", "i", "o", "u"}

        max_vowels = sum([1 for c in s[:k] if c in vowels])
        cur_vowels = max_vowels

        for i in range(k, len(s)):
            add = int(s[i] in vowels)
            drop = int(s[i-k] in vowels)
            cur_vowels = cur_vowels + add - drop

            if cur_vowels > max_vowels:
                max_vowels = cur_vowels
                if max_vowels == k:
                    return max_vowels
        return max_vowels
        