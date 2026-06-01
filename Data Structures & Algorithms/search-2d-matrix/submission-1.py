class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # traverse outer list, 2 pointers, compare against values of the first element of inner lists
        # do binary to zero in on the inner list, then do binary search on inner list
        i, j = 0, len(matrix) - 1
        while i <= j:
            mid = (i+j) // 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                j = mid - 1
            else:
                i = mid + 1
        if j < 0:
            return False

        lo, hi = 0, len(matrix[j])-1
        while lo <= hi:
            mid = (lo+hi) // 2
            if target == matrix[j][mid]:
                return True
            if target < matrix[j][mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False