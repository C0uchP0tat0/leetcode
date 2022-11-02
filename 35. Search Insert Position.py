from collections import defaultdict


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        d=defaultdict(int)
        nums.append(target)
        nums = sorted(nums)
        indexes = [i for i in range(len(nums))]
        for i,j in zip(nums, indexes):
            if i in d:
                return d[i]
            else:
                d[i]=j
        return d[target]
        
        
def main():
    nums = [1,3,5,6]
    target = 5
    y=Solution()
    y.searchInsert(nums, target)


if __name__ == "__main__":
    main()