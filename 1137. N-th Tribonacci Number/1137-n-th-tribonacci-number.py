# Runtime 0 ms

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return min(n,1)
        
        f = [0] * (n+1)
        f[1] = 1
        f[2] = 1

        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2] + f[i-3]
        return f[-1]
            
        