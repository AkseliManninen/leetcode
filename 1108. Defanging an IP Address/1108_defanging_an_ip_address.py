# Runtime 34 ms

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")