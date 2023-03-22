class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = list()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
        return result


def main():
    nums = [3,2,4]
    target = 6
    y=Solution()
    y.twoSum(nums, target)
    
if __name__ == "__main__":
    main()
