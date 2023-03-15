from collections import defaultdict

class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=1:
            return s
        d=defaultdict(list)
        iter_num=0
        for i in range(0, len(s), numRows+(numRows-2)):
            print(s[i:numRows+i])
            for k in range(len(s[i:numRows+i])):
                d[k].append(s[i:numRows+i][k])
            # print(s[i:numRows+i])
            
        for j in range(-1, len(s), numRows+numRows-2):
            print(s[j])
            if j==-1:
                pass
            else:
                if iter_num==0:
                    iter_num+=1
                else:
                    iter_num+=2
                zip_el = list(zip(s[j-numRows+3:j+1], range(numRows-2, 0, -1)))
                for i in zip_el:
                    d[i[1]].insert(iter_num, i[0])
                    print(i)
                # for k, in ranges[j-numRows+3:j+1], range(numRows-2)):
                # print(list(zip(s[j-numRows+3:j+1], range(numRows-2, 0, -1))))
                    # for l in range(numRows-2):
                    # print(k, l)
                    # print(k, iter_num)
                    # d[k].append(s[i:numRows+i][k])
                # print(j)
                # print(s[j-numRows+3:j+1])
        print(d)
        s1=''.join([x for l in d.values() for x in l])
        # print(s1)
        # return s1

        
        
        
        
    

def main():
    # s = "PAYPALISHIRING"
    # numRows = 3
    # Output: "P A H N
    #          APLSIIG
    #          Y I R"
    # s = "PAYPALISHIRING"
    # numRows = 4
    # s = "A"
    # numRows = 1
    s = "ABCDE"
    numRows = 4
    
    # Output: "PINALSIGYAHRPI"
    # Explanation:
    #         P     I    N
    #         A   L S  I G
    #         Y A   H R
    #         P     I
    y=Solution()
    y.convert(s, numRows)
    
if __name__ == "__main__":
    main()