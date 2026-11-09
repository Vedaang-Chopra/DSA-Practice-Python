class Solution:
    def isValid(self, s: str) -> bool:
        stack_pop = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }
        stack =[]

        for i in list(s):
            if i =='(' or i=='{' or i=='[':
                stack.append(i)
            
            
            if (i ==')' or i== '}' or i== ']'):
                if len(stack)==0:
                    return False
                else:
                    char = stack.pop()
                    if i ==')' and char == stack_pop[i]:
                        continue
                    if i =='}' and char == stack_pop[i]:
                        continue
                    if i ==']' and char == stack_pop[i]:
                        continue
                    else:
                        return False
                

        if len(stack) >0:
            return False
        else:
            return True


