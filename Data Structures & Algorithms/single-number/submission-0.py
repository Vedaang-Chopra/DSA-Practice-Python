from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        index =0
        i=0
        print(nums)
        while i<=len(nums)-1:
            print(i, nums[i])
            
            if i>=len(nums)-1:
                index =i
                print(index)
                break
            
            if nums[i]==nums[i+1]:
                i=i+2
                print("Next Index")
                continue
            else:
                index=i 
                break
        return nums[index]
        