class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = []
        l = len(digits)-1
        while l>=0:
            if l==0:
                if digits[l]==9:
                    digits[l]=0
                    digits.insert(0,1)
                    break
                else:
                    digits[l]+=1
                    break

            if digits[l]==9:
                digits[l]=0
                l=l-1
            else:
                digits[l]+=1
                break
            
        return digits

