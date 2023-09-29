from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        d=defaultdict()
        len_nums=len(nums)
        for i in range(len_nums):
            for j in range(i+1, len_nums):
                for k in range(j+1, len_nums):
                    if sum([nums[i], nums[j], nums[k]])==0:
                        d[frozenset([nums[i], nums[j], nums[k]])]=[nums[i], nums[j], nums[k]]
                    else:
                        pass
        return d.values()
            
        
                
                
            
        
        
        
def main():
    nums = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]
    # Explanation: 
    # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    # The distinct triplets are [-1,0,1] and [-1,-1,2].
    # Notice that the order of the output and the order of the triplets does not matter.
    y=Solution()
    y.threeSum(nums)


if __name__ == "__main__":
    main()
