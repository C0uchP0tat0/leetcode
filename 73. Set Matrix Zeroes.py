class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import copy
        index_j=0
        matrix1=[]
        for i in range(len(matrix)):
            matrix1.append(copy.deepcopy(matrix[i]))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    index_j=j
                    for k in range(len(matrix[i])+len(matrix)):
                        try:
                            matrix1[i][k]=0
                            matrix1[k][index_j]=0
                        except IndexError:
                            try:
                                matrix1[k][index_j]=0
                            except IndexError:
                                pass
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix1[i][j]==matrix[i][j]:
                    pass
                else:
                    matrix[i][j]=0
        return matrix
        
        
def main():
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # Output: [[1,0,1],[0,0,0],[1,0,1]]
    # matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    # matrix = [[0],[1]]
    matrix = [[1],[0],[3]]
    # Output: [[0],[0],[0]]
    y=Solution()
    y.setZeroes(matrix)


if __name__ == "__main__":
    main()