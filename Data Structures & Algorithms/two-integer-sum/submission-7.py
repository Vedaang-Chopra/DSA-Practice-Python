class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs ={}
        indices =[]
        for i in range(0,len(nums)):
            current_val = nums[i]
            reqd_val = target-current_val
            # print(i, current_val, reqd_val, pairs.get(reqd_val, False))
            val = pairs.get(reqd_val, None)
            # if reqd_val in pairs:
            if val is not None:
                indices.append(pairs.get(reqd_val))
                indices.append(i)
                return indices
            else:
                pairs[current_val] = i
            # print(pairs, indices)
            # print()
        return indices