from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d=defaultdict(int)
        for i in range(len(board)):
            d=defaultdict(int)
            for j in board[i]:
                if j=='.':
                    pass
                else:
                    d[j]+=1
                    if d[j]>1:
                        return False
        for i in range(len(board)):
            d=defaultdict(int)
            for j in range(len(board)):
                if board[j][i]=='.':
                    pass
                else:
                    # print(board[j][i])
                    d[board[j][i]]+=1
                    if d[board[j][i]]>1:
                        return False
        for i in range(len(board)):
            d=defaultdict(int)
            if i==0 or (i % 3 ==0):
                for j in board[i][0:3]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
                for j in board[i+1][0:3]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
                for j in board[i+2][0:3]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
            elif i==1 or i==4 or i==7:
                for j in board[i-1][3:6]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
                for j in board[i][3:6]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
                for j in board[i+1][3:6]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
            else :
                for j in board[i-2][6:]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
                for j in board[i-1][6:]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
                for j in board[i][6:]:
                    if j=='.':
                        pass
                    else:
                        d[j]+=1
                        if d[j]>1:
                            return False
        return True
    
    def checkIsDot(self, el):
        if el=='.':
            return None
        else:
            return el
        
        
        
def main():
    # board = [["5","3",".",".","7",".",".",".","."]
    #         ,["6",".",".","1","9","5",".",".","."]
    #         ,[".","9","8",".",".",".",".","6","."]
    #         ,["8",".",".",".","6",".",".",".","3"]
    #         ,["4",".",".","8",".","3",".",".","1"]
    #         ,["7",".",".",".","2",".",".",".","6"]
    #         ,[".","6",".",".",".",".","2","8","."]
    #         ,[".",".",".","4","1","9",".",".","5"]
    #         ,[".",".",".",".","8",".",".","7","9"]]
    # Output: true
    # board = [[".",".",".",".","5",".",".","1","."]
    #         ,[".","4",".","3",".",".",".",".","."]
    #         ,[".",".",".",".",".","3",".",".","1"]
    #         ,["8",".",".",".",".",".",".","2","."]
    #         ,[".",".","2",".","7",".",".",".","."]
    #         ,[".","1","5",".",".",".",".",".","."]
    #         ,[".",".",".",".",".","2",".",".","."]
    #         ,[".","2",".","9",".",".",".",".","."]
    #         ,[".",".","4",".",".",".",".",".","."]]
    # Output: false
    board = [[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".","6",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".","8",".",".",".","."]
            ,["9",".",".",".","7","5",".",".","."]
            ,[".",".",".",".","5",".",".","8","."]
            ,[".",".","9",".",".",".",".",".","."]
            ,["2",".","6",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]]
    # Output: false
    y=Solution()
    y.isValidSudoku(board)


if __name__ == "__main__":
    main()
