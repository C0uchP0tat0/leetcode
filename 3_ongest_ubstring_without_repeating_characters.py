from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==" ":
            return 1
        elif s=="":
            return 0
        res_count = 0
        st=s[:]+s[-1]
        for i in range(len(st)):
            d = defaultdict(int)
            count = 0
            for j in st[i:]:
                d[j]+=1
                if d[j]==1:
                    count+=1
                else:
                    if count>res_count:
                        res_count=count
                        break
                    else:
                        break
        return res_count
            
        
    

def main():
    s="au"
    x=Solution()
    x.lengthOfLongestSubstring(s)
    
if __name__ == "__main__":
    main()