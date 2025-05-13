class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        org = x
        while x>0:
            reverse = reverse * 10 + x%10
            x = x//10

        return (org==reverse)

        