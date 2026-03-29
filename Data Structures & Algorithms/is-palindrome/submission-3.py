class Solution:
    def isPalindrome(self, s: str) -> bool:
        current_string = "".join(list(filter(lambda x: x.isalnum(), s.lower().strip())))
        reverse = current_string[::-1]
        print(current_string, reverse)
        return current_string ==reverse