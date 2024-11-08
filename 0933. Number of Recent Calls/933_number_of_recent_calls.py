# Time complexity: O(n)
# Space complexity: O(n)

class RecentCounter(object):

    def __init__(self):
        self.counter = 0
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        self.pings = list(filter(lambda x: x >= t - 3000, self.pings))
        self.counter = len(self.pings)
        return self.counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)