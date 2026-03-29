# from collections import Counter

class Solution:
    def  counter(self, s):
        counter_dict={}
        for i in s:
            if i in counter_dict:
                counter_dict[i]+=1
            else:
                counter_dict[i]=1
        return counter_dict
    def isAnagram(self, s: str, t: str) -> bool:
        s_char, t_char = self.counter(s),self.counter(t)
        if s_char ==t_char:
            return True
        else:
            return False