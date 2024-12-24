class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def is_concatenation(s, t):
            return s == t * (len(s) // len(t))
        
        gcd_length = gcd(len(str1), len(str2))
        candidate = str1[:gcd_length]
        
        if is_concatenation(str1, candidate) and is_concatenation(str2, candidate):
            return candidate
        
        return ""