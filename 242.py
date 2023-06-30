"""
# first mmethod:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_letter_count = {}
        l_letter_count = {}
        for l in s:
            s_letter_count[l]=0
        for l in s:
            s_letter_count[l]+=1    
        for l in t:
            l_letter_count[l]=0
        for l in t:
            l_letter_count[l]+=1
        if s_letter_count == l_letter_count:
            return True    
count letters in every strings and save in dict
if dict is the same  True
"""

"""
Second method:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_letter_count = {}
        t_letter_count = {}
        for l in s:
            s_letter_count[l]=1+s_letter_count.get(l,0) 
        for l in t:
            t_letter_count[l]=1+t_letter_count.get(l,0) 
        if s_letter_count == t_letter_count:
            return True    

Use get method to get the value in dict
If the value is 0 we could set a default number '0' or any number in secone variable in get function  get(key, default value)             

"""


"""
Third method:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_letter_count = {}
        for l in s:
            s_letter_count[l]=1+s_letter_count.get(l,0) 
        for l in t:
            try:
                s_letter_count[l]=s_letter_count[l]-1
                if s_letter_count[l]<0:
                    return False
            except:
                return False
        return True

Use minus  
"""
