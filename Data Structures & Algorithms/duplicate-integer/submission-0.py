class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp ={}
        for i in range(0,len(nums)):
            if nums[i] in temp:
                temp[nums[i]] +=1
                # print(temp)
                return True
            else:
                temp[nums[i]] = 1
        return False
        