class Solution:
    def binary_search(self, arr, target):
        p_start=0 
        p_end =len(arr)-1
        while p_start<=p_end:
            mid = p_start +  (p_end-p_start)//2
            if target < arr[mid]:
                p_end = mid-1
            elif target > arr[mid]:
                p_start = mid +1
            else:
                return mid
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix ==[]:
            return False
        
        if len(matrix)==1:
            if self.binary_search(matrix[0], target) ==-1:
                return False
            else:
                return True
            
        ## Step-1: - Figuring out the right row
        first_col = []
        search_row = len(matrix)-1
        i=0
        for col in zip(*matrix):
            for element in col:
                print(element, i, target)
                if element > target:
                    break
                else:
                    search_row=i
                    i=i+1
                    # print(search_row, i)
            break
        print(target, search_row, matrix[search_row])

        ## Step-2: - Binary Search on Row
        if self.binary_search(matrix[search_row], target) ==-1:
            return False
        else:
            return True
        
        