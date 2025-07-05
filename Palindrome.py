class Solution(object):
    def isPalindrome(self, x):
        reversed = str(x)[::-1]
        if str(x) == reversed:
            return True 
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """
        
