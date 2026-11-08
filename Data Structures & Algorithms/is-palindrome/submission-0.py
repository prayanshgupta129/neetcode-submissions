class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = ''
        for c in s :
            if c.isalnum() :
               z += c 
        z = z.upper()
    
        return z == z[::-1]


        