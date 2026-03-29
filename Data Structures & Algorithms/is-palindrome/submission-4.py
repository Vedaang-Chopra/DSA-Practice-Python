class Solution:
    def isPalindrome(self, s: str) -> bool:
        # current_string = "".join(list(filter(lambda x: x.isalnum(), s.lower().strip())))
        # reverse = current_string[::-1]
        # print(current_string, reverse)
        # return current_string ==reverse

        l, r = 0, len(s)-1
        while l<r:

            print(s[l], s[r], )
            while l<r and not s[l].isalnum():
                l+=1
                print("Non l alp")
            
            while r>l and not s[r].isalnum():
                r-=1
                print("Non r alp")

            if s[l].lower() != s[r].lower():
                return False
            
            l,r = l+1, r-1
        return True