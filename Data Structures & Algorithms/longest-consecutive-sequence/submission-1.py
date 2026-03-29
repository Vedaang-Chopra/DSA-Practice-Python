class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        all_unique_numbers = set(nums)
        longest_sequence =0


        for current_val in all_unique_numbers:
             if current_val-1 not in all_unique_numbers:
                length=1
                while (current_val+length) in all_unique_numbers:
                    length+=1
                longest_sequence = max(length, longest_sequence)
        return longest_sequence
