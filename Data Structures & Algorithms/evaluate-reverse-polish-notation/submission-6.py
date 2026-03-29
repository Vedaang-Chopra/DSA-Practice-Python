class Solution:


    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        if len(tokens)==0:
            return 0
        
        for i in range(0,len(tokens)):
            current_val = tokens[i]
            print(current_val)
            if current_val.strip() =='+':
                val_2 = stack.pop()
                val_1 = stack.pop()
                val = val_1 + val_2
                stack.append(val)
                print(val)
            elif current_val.strip() =='-':
                val_2 = stack.pop()
                val_1 = stack.pop()
                val = val_1 - val_2
                stack.append(val)
                print(val)
            elif current_val.strip() =='*':
                val_2 = stack.pop()
                val_1 = stack.pop()
                val = val_1 * val_2
                stack.append(int(val))
                print(val)
            elif current_val.strip() =='/':
                val_2 = stack.pop()
                val_1 = stack.pop()
                if val_1==0:
                    val=0
                else:
                    val = val_1 / val_2
                stack.append(int(val))
                print(val)
            else:
                stack.append(int(current_val))
            
        return int(stack.pop())
            