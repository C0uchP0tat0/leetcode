from collections import defaultdict


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
            if d[i]>1:
                return i
        
        
def main():
    nums = [1,3,4,2,2]
    # Output: 2
    y=Solution()
    y.findDuplicate(nums)


if __name__ == "__main__":
    main()
