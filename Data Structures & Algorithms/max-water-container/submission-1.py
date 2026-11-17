import math
class Solution:
    

    def calculate_water(self, heights, left, right):
        base_water = abs(right -left)
        height_water = min(heights[left], heights[right])
        water_total = base_water * height_water
        return water_total

    def maxArea(self, heights: List[int]) -> int:
        left =0; right =len(heights)-1
        max_water =0
        while left<=right:
            current_water= self.calculate_water(heights, left, right)
            if current_water >max_water:
                max_water =  current_water

            if heights[left] <heights[right]:
                left +=1
            else:
                right-=1
        return max_water