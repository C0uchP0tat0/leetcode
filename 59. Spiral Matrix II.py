from collections import defaultdict


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # if n ==5:
        #     return [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
        sqr_n=n*n
        # number=0
        list_index=0
        d=defaultdict(int)
        d_list=defaultdict(list)
        exit_list=[]
        # for i in range(sqr_n):
        #     number+=1
        #     d[i]=number
        number=n
        k=n-1
        for i in range(n):
            if i==0:
                d_list[i]=[j for j in range(1,n+1)]
            elif i==n-1:
                l=[]
                for j in range(n):
                    number+=1
                    l.insert(0, number)
                d_list[i]=l
            else:
                number+=1
                d_list[i].append(number)
        # for i in range(1 ,n):
        #     number+=1
        #     d_list[i][-1]=number
        # for i in range(1 ,n):
        #     number+=1
        #     k-=1
        #     d_list[n-1][k]=number
        # for i in range(n-2, 0, -1):
        #     number+=1
        #     d_list[i][0]=number
        # for j in range(1, n-1):
        #     if j % 2 !=0:
        #         for i in range(1, n-1):
        #             number+=1
        #             d_list[j][i]=number
        #             print(number)
            # else:
            #     for i in range(n-2, 0, -1):
            #         number+=1
            #         d_list[j][i]=number
        print([i for i in d_list.values()])
        return [i for i in d_list.values()]      
# [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
# [[1,2,3,4,5],[16,17,18,19,6],[15,22,21,20,7],[14,23,24,25,8],[13,12,11,10,9]]
# [[1,2,3,4,5,6],[20,21,22,23,24,7],[19,28,27,26,25,8],[18,29,30,31,32,9],[17,36,35,34,33,10],[16,15,14,13,12,11]]
[[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]

def main():
    n = 5
    y=Solution()
    y.generateMatrix(n)


if __name__ == "__main__":
    main()