class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        
        if len(s)==1:
            return 1
        l=0 
        sub_s= set()
        longest=0
        for r in range(len(s)):
            while s[r] in sub_s:
                sub_s.remove(s[l])
                l+=1
        
            w=r-l+1
            longest= max(longest,w )    
            sub_s.add(s[r])
                
                
        return longest



        