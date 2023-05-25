class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        if len(res)==0:
            return [-1,-1]
        elif  len(res)==1:
            res.append(res[0])
            return res
        else:
            return [res[0], res[-1]]
            
        
        
def main():
    nums = [5,7,7,8,8,10]
    target = 8
    # Output: [3,4]
    y=Solution()
    y.searchRange(nums, target)


if __name__ == "__main__":
    main()
