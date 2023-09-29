class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False
            
        
            


def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    # Output: true
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    # Output: false
    y=Solution()
    y.searchMatrix(matrix, target)


if __name__ == "__main__":
    main()
