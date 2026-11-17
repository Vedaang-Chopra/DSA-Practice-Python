class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0; right =len(numbers)-1

        while left<=right:
            current_sum = numbers[left] + numbers[right]
            # print(f"{left}:{numbers[left]}, {right}:{numbers[right]}, {current_sum}, {target}")
            if current_sum ==target:
                return [left+1, right+1]
            else:
                if current_sum < target:
                    left+=1
                else:
                    right-=1
        return [-1, -1]



