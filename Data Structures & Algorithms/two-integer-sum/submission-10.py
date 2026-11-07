class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs ={}

        for i in range(0,len(nums)):
            needed_pair = target - nums[i]
            
            if pairs.get(nums[i], None) != None:
                if pairs[nums[i]] != i:
                    return [pairs[nums[i]], i]
            else:
                pairs[needed_pair] = i
                # pairs[needed_pair].append(i)
            # print(i, nums[i], needed_pair , pairs)
        return [-1, -1]