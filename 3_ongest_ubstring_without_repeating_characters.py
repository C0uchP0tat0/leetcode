class Solution:
    def __init__(self):
        self.len_res_list=0
        self.count=0
        
    def result(self):
        print(self.len_res_list)
        return self.len_res_list
    
    def crop_list(self, s):
        s=s[1:]
        self.lengthOfLongestSubstring(s)
        return s
    
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        res_list=list()
        print(s)
        if len(s)>self.len_res_list:
            for i in s:
                # print(res_list)
                if i not in res_list:
                    res_list.append(i)
                    if len(res_list)>self.len_res_list:
                        self.len_res_list=len(res_list)
                else:
                    if len(res_list)>self.len_res_list:
                        self.len_res_list=len(res_list)
                    res_list.clear()
                    res_list.append(i)
            s=self.crop_list(s)
            self.count+=1
        self.result()
        
    

def main():
    s = "abcabcbb"
    x=Solution()
    x.lengthOfLongestSubstring(s)
    
if __name__ == "__main__":
    main()