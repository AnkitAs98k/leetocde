class Solution(object):
    def isPalindrome(self, x):
        b = x
        sum =0

        while(x>0):
            rem = x % 10
            sum = sum*10 + rem
            x= x//10
        if (b == sum):
            return True
        else:
           return False
        