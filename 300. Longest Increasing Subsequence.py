class Solution:
    def __init__(self):
        self.c=0
        
    def lengthOfLIS(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            self.make_res(nums[i], nums[i:])
        # print(self.c)
        # res=[]
        # for i in range(len(nums)):
        #     e = nums[i]
        #     try:
        #         if nums[i]<e:
        #             pass
        #         else:
        #             res.append(nums[i])
        #     except IndexError:
        #         pass
        # self.count_out(e, res)
    
    def make_res(self, e, l):
        # print(e, l)
        res=[]
        max_element = 0
        res.append(e)
        for i in range(1, len(l)):
            try:
                if l[i]<e:
                    pass
                else:
                    if l[i]==e:
                        pass
                    else:
                        if l[i]>max_element:
                            max_element=l[i]
                        res.append(l[i])
            except IndexError:
                pass
        for i in range(len(res)-1, -1, -1):
            if res[i]==max_element:
                res=res[:i+1]
                break
                
        print(e, res)
        self.count_out(e, res)
    
    def count_out(self, e, res):
        max_element=res[-1]
        for i in range(1, len(res)-1):
            pass
        # print(max_element)
        # print(e, res)
        # try:
        #     el = res[1] 
        # except IndexError:
        #     pass
        # for i in range(1, len(res[0:])):
        #     try:
        #         if el<res[i]:
        #             el=res[i]
        #         else:
        #             try:
        #                 # print(res)
        #                 el=res[i+1]
        #                 res.pop(i)
        #             except IndexError:
        #                 res.pop(i)
        #     except IndexError:
        #         pass
        # print(e, res)
            
        
    
            
        # for j in range(len(res[1:])):
        #     try:
        #         if 
        #     except IndexError:
        #         pass
                
        # print(e, res)
     
        # if c > self.c:
        #     self.c = c
        
        
        
def main():
    nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    # nums = [0,1,0,3,2,3]
    # Output: 4
    # nums = [7,7,7,7,7,7,7]
    # Output: 1
    y=Solution()
    y.lengthOfLIS(nums)


if __name__ == "__main__":
    main()
