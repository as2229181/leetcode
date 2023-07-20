"""
reversed 
 r = "".join(reversed(new_str)) could also writed as new_str[::-1]
 time complexity = n  sapce n 
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                new_str += i.lower()
        r = "".join(reversed(new_str))        
        return new_str == r
    
"""
use while loop 

n+n/2
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                new_str += i.lower()
        l = 0
        r = len(new_str)-1
        while l < r:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1
        return True
    
"""
Not use reversed
time complexity  n 
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and s[l].isalnum() is False:
                l += 1
            while l < r and s[r].isalnum() is False:
                r -= 1 
            l_letter = s[l].lower()
            r_letter = s[r].lower()        
            if l_letter != r_letter:
                return False
            l += 1
            r -= 1     
        return True