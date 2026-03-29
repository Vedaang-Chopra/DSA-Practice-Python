class Solution:
    def check_pair(self, start:str, end:str):
        if start=='(' and end==')':
            return True
        elif start=='{' and end=='}':
            return True
        elif start=='[' and end==']':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        arr = []
        if len(s)==0:
            return True
        
        if len(s)>0:
            if '(' not in s and '[' not in s and '{' not in s:
                return False

        for i in range(0,len(s)):
            CURRENT_CHAR = s[i]
            if CURRENT_CHAR == '}' or CURRENT_CHAR == ']' or CURRENT_CHAR == ')':
                if len(arr)==0:
                    return False
                ele = arr.pop()
                if self.check_pair(ele, CURRENT_CHAR):
                    continue
                else:
                    return False
                print("Status after pop:",arr, ele)
            else:
                arr.append(CURRENT_CHAR)
            
        if len(arr)>0:
            return False
        else:
            return True

            