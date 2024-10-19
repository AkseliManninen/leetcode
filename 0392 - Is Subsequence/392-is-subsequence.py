# Runtime 0 ms

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_i = 0
        t_i = 0

        while t_i < len(t) and s_i < len(s):
            if s[s_i] == t[t_i]:
                s_i += 1
                t_i += 1
            else:
                t_i += 1

        return s_i == len(s)

