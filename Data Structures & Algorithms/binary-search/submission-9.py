class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid= start + (end-start)//2
            # print(start, end, mid)
            # print(nums[start], nums[end], nums[mid], target)
            # print()
            if target==nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid -1
            else:
                start = mid +1
            
        return -1

        
