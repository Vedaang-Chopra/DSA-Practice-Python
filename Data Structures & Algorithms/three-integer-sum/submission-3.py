class Solution:
    def twosum(self, nums, current_sum, index_to_avoid):
        i, j = 0, len(nums) - 1
        pairs = []
        while i < j:
            if i == index_to_avoid:
                i += 1
                continue
            if j == index_to_avoid:
                j -= 1
                continue

            s = nums[i] + nums[j]
            if s < current_sum:
                i += 1
            elif s > current_sum:
                j -= 1
            else:
                pairs.append([i, j])
                i += 1
                j -= 1

        if not pairs:
            return [[-1, -1]]
        return pairs    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        final_pairs= set()
        for i in range(0,len(nums_sorted)):
            current_var = nums_sorted[i]
            pairs=self.twosum(nums_sorted, current_var*-1, i)
            indices_i, indices_j = pairs[0][0], pairs[0][1]
            # print("Indices:")
            # print(current_var, indices_i, indices_j)
            # print("Sum:")
            # print(nums_sorted[i], nums_sorted[indices_i], nums_sorted[indices_j])
            print("Current_var:", current_var)
            print(pairs)
            if indices_i ==-1 or indices_j==-1:
                continue
            else:
                for j in pairs:
                    v1, v2= nums_sorted[j[0]], nums_sorted[j[1]]
                    current_pair = [v1, v2, current_var]
                    # if sorted(current_pair) in final_pairs:
                    #     continue
                    # else:
                    final_pairs.add(tuple(sorted(current_pair)))
                print(final_pairs)
        return (list(final_pairs))