class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char = sorted(list(s1))
        print(s1_char)
        for r in range(len(s2)):
            if s2[r] in s1_char:
                if sorted(list(s2[r:r+len(s1)]))==s1_char:
                    return True
                else:
                    continue
        return False

                    
        
            