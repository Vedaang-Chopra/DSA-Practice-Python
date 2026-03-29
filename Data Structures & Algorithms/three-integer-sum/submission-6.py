import copy

class Solution:
    def two_sum(self, i, nums:List[int], target:int, ex_index:int):
        indices =[]
        start, end = i+1, len(nums)-1
        while start<end:
            # print(ex_index, target, start, end, nums[start], nums[end], nums[start]+nums[end] )
            if nums[start] + nums[end] ==target:
                if [nums[start], nums[end], nums[ex_index]] in indices:
                    pass
                else:
                    indices.append([nums[start], nums[end], nums[ex_index]])
                start+=1
                end-=1
            elif nums[start] + nums[end] >target:
                end =end-1
            else:
                start = start+1
        return indices
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices =[]
        target =0
        nums.sort()
        for i in range(0,len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            current_val = nums[i]
            target_reqd = target - current_val
            indices+=self.two_sum(i, nums, target_reqd, i)
            print()
            
        return indices