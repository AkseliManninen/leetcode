# Runtime 21 ms

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split(" ")
        rev_s = ""

        for i in range(len(words)):
            word = strip(words[len(words) -1 - i])
            if word != "":
                rev_s += word + " "
        return strip(rev_s)