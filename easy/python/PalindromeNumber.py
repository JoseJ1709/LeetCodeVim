class Solution(object):
    def isPalindrome(self,x):
        if x < 0:
            return False
        z = str(x)[::-1]
        return str(x) == z