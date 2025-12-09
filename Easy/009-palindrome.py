class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        r = 0
        if x < 0:
            return False
        else :
            while x > 0 :
                r = (r * 10) + (x % 10)
                x = x // 10
            if y == r:
                return True
            else :
                return False
        
        
